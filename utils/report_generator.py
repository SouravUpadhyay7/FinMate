from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_pdf(results, pie_chart_buffer=None):
    buffer = BytesIO()
    # Use a wider page margin to give more space for content
    doc = SimpleDocTemplate(buffer, pagesize=letter, 
                           rightMargin=0.5*inch, leftMargin=0.5*inch,
                           topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    elements = []
    
    # Add title
    title_style = styles['Heading1']
    elements.append(Paragraph("FinMate Financial Report", title_style))
    elements.append(Spacer(1, 20))
    
    # Add financial analysis section
    elements.append(Paragraph("Financial Analysis", styles['Heading2']))
    elements.append(Spacer(1, 10))
    
    # Create a table for the financial results with word wrapping
    data = []
    for key, value in results.items():
        if key == 'investment_advice':  # Skip, we'll add this separately
            continue
            
        if isinstance(value, (int, float)):
            formatted_value = f"₹{value:,.2f}" if key not in ['family_size'] else str(value)
        else:
            formatted_value = str(value)
        data.append([key.replace('_', ' ').title(), formatted_value])
    
    # Create the table with more width
    if data:
        # Adjust column widths to use more of the page width
        table = Table(data, colWidths=[250, 250])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('WORDWRAP', (0, 0), (-1, -1), True),  # Enable word wrapping
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),   # Align text to top of cell
        ]))
        elements.append(table)
    
    # Add savings and budget recommendations
    if 'recommended_savings' in results:
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("Recommendations", styles['Heading2']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(f"Recommended Monthly Savings: ₹{results.get('recommended_savings', 0):,.2f}", styles['Normal']))
        elements.append(Paragraph(f"Budget Health: {results.get('budget_health', 'N/A')}", styles['Normal']))
    
    # Add the pie chart if available
    if pie_chart_buffer:
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("Expense Breakdown", styles['Heading2']))
        elements.append(Spacer(1, 10))
        
        # Create the image and scale it appropriately
        pie_chart_image = Image(pie_chart_buffer, width=400, height=300)
        elements.append(pie_chart_image)
    
    # Check if investment advice exists in results
    if 'investment_advice' in results:
        elements.append(Spacer(1, 20))
        elements.append(Paragraph("Investment Advice", styles['Heading2']))
        elements.append(Spacer(1, 10))
        for tip in results['investment_advice']:
            elements.append(Paragraph(f"• {tip}", styles['Normal']))
            elements.append(Spacer(1, 5))
    
    # Build the PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer