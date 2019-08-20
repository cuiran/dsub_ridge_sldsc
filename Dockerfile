FROM google/cloud-sdk:slim

RUN git clone https://github.com/cuiran/ldsc_ridge.git /home/ldscore/
RUN chmod 777 -R /home/ldscore/
RUN pip install --upgrade cython
RUN apt-get -y install g++


COPY requirements.txt /home/

RUN pip install -r /home/requirements.txt

VOLUME ["/root/.config"]
CMD [ "/bin/bash" ]
