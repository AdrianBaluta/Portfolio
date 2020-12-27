import PyPDF2
import sys

inputs = sys.argv[1:]
input_file = "super.pdf"
output_file = "super_wtr.pdf"
watermark_file = "wtr.pdf"

with open(input_file, "rb") as filehandle_input:
	pdf = PyPDF2.PdfFileReader(filehandle_input)
	with open ('wtr.pdf', 'rb') as filehandleWatermark:
		watermark = PyPDF2.PdfFileReader(filehandleWatermark)
		firstPage = pdf.getPage[:]
		firstPageWatermark = watermark.getPage[:]
		firstPage.mergePage(firstPageWatermark)
		pdfWriter = PyPDF2.PdfFileWriter()
		pdfWriter.addPage(firstPage)

		with open (output_file, 'wb') as filehandleOutput:
			pdfWriter.write(filehandleOutput)


