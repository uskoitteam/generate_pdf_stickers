############################################################
### Script generates pdf file for stickers with PC names ###
### Designed by Maksym Tsybulskyi, 2024 ###
############################################################

from reportlab.lib.pagesizes import inch
from reportlab.pdfgen import canvas
font = "Helvetica-Bold"

def generate_pdf(names, output_file):
    # Set page size to 6"x4"
    page_width = 6 * inch
    page_height = 4 * inch

    # Create a PDF canvas
    c = canvas.Canvas(output_file, pagesize=(page_width, page_height))

    for name in names:
        # Set the font on each page to ensure consistency
        c.setFont(font, 60)  # Adjust the font size as needed

        # Set the position for writing the name in the center of the page
        text_width = c.stringWidth(name, font, 60)
        x_position = (page_width - text_width) / 2  # Center horizontally
        y_position = (page_height / 2)  # Center vertically

        # Draw the name on the page
        c.drawString(x_position, y_position, name)

        # Add a new page for the next name
        c.showPage()

    # Save the PDF
    c.save()


# Example usage:
names = []
template = "USKO-"
for i in range(5001, 5041, 1):
    name = f"{template}{i}"
    names.append(name)
generate_pdf(names, "names_list_per_page_4x6.pdf")
