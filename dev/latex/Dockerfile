FROM qmcgaw/latexdevcontainer:latest-full

RUN apt update && apt install -y ghostscript libfontconfig1 fontconfig libfontconfig1-dev libfontconfig python3-pip && \
    pip3 install Pygments && \
    apt clean
CMD bash
