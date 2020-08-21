FROM ubuntu:focal 

COPY source/make.py .
COPY source/impl.py .
COPY file_lists/lf.txt .
COPY file_lists/plf.txt .
COPY file_lists/vfa.txt .
COPY file_lists/qc.txt .

RUN apt-get update 
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y wget wkhtmltopdf texlive-extra-utils python

CMD ["python", "make.py"]
