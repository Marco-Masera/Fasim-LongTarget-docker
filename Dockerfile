FROM debian
MAINTAINER Ivan Molineris <ivan.molineris@unito.it>

ENV LANG=C LC_ALL=C
RUN apt-get update 
RUN apt-get install -y g++ python3 && apt-get clean
ADD . /usr/tmp/installer/
RUN g++ /usr/tmp/installer/Fasim-LongTarget.cpp /usr/tmp/installer/ssw_cpp.cpp /usr/tmp/installer/sswNew.cpp -O -msse2 -o /usr/bin/fasim
ENTRYPOINT ["/usr/bin/fasim"]
