import sys
from weasyprint import HTML

def get_file_names():
  if len(sys.argv) < 2:
    print('HTML file name not provided')
    exit
  HTML_file_name = sys.argv[1]
  pdf_file_name = HTML_file_name + '.pdf'
  if len(sys.argv) >= 3:
    pdf_file_name = sys.argv[2]

  return (HTML_file_name, pdf_file_name)

def generate_pdf_from_html(HTML_file_name, pdf_file_name):
  HTML(HTML_file_name).write_pdf(pdf_file_name)

def main():
  HTML_file_name, pdf_file_name = get_file_names()
  generate_pdf_from_html(HTML_file_name, pdf_file_name)

if __name__ == '__main__':
  main()
