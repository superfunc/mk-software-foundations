import os, sys

def run_cmd(cmd):
  print('Running cmd: ' + cmd)
  os.system(cmd)

def read_inputs(name):
  contents = []
  with open("../" + name + ".txt", 'r') as f:
    contents = f.readlines()
  return map(lambda s: s.strip(), contents)

def run_gen(name, file_base_names):
  output_dir = "/var/generated/pdf/"
  
  html_file_names = map(lambda s: s + ".html", file_base_names)
  pdf_file_names = map(lambda s: output_dir + s + ".pdf", file_base_names)
  
  generate_cmd = "wkhtmltopdf "
  combine_cmd = "pdfjam --fitpaper=false --rotateoversize=false " 
  run_cmd("mkdir -p " + output_dir)

  for (f, h) in zip(file_base_names, html_file_names):
    run_cmd(generate_cmd + "%s /var/generated/pdf/%s.pdf" % (h,f))

  run_cmd(combine_cmd + " ".join(pdf_file_names) + " -o " + book_name + ".pdf")

expected_names = ["lf", "plf", "vfa", "qc"]

if len(sys.argv) != 2:
    sys.exit("Wrong number of inputs, expected ./<prog> " + "|".join(expected_names))

book_name = sys.argv[1]
if book_name not in expected_names:
    sys.exit("Invalid name, expected " + "|".join(expected_names))

run_gen(book_name, read_inputs(book_name))
