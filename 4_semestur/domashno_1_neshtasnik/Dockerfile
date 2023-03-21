FROM ubuntu:latest

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends pandoc texlive-latex-base texlive-fonts-recommended texlive-extra-utils texlive-latex-extra

# bulgarian
RUN apt-get install -y --no-install-recommends texlive-lang-cyrillic cm-super

RUN mkdir /data

WORKDIR /data

ENTRYPOINT ["pandoc"]
