import os, sys, shutil

def cmd(cmd):
  print('Running cmd: ' + cmd)
  os.system(cmd)

def gen_pdf(name):
  output_dir = "/var/generated/pdf/"
  archive_name = name + ".tgz"
  directory_name = name
  output_name = name + ".pdf"
  root_page = ("https://softwarefoundations.cis.upenn.edu/" 
               + name 
               + "-current/" 
               + archive_name)

  cmd("mkdir -p " + output_dir)
  cmd("wget " + root_page)
  cmd("tar xf " + archive_name)
  os.chdir(directory_name)
  cmd("python2 ../impl.py " + name)
  cmd("cp " + output_name + " ../" + output_dir)
  os.chdir("..")

def clean_extra_pdf(names):
  generated_names = map(lambda s: s + ".pdf", names) 
  generated_dir = "/var/generated/pdf/"
  files = os.listdir(generated_dir)
  for f in files:
    base = os.path.basename(f)
    if base not in generated_names:
      os.remove(generated_dir + f)

def clean_downloaded_files(names):
  for name in names:
    archive_name = name + ".tgz"
    directory_name = name
    os.remove(archive_name)
    shutil.rmtree(directory_name)

def clean(names):
  clean_extra_pdf(names)
  clean_downloaded_files(names)

# -- Logic Foundations (lf)
# -- Programming Language Foundations (plf)
# -- Verified Functional Algorithms (vfa)
# -- QuickChick Testing (qc)
names = ["lf", "plf", "vfa", "qc"]
for name in names:
  gen_pdf(name)

clean(names)
