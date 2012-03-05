cd ~/Downloads/

wget http://pyglet.googlecode.com/files/pyglet-1.1.4.zip
unzip pyglet-1.1.14.zip
cd pygle*
sudo python setup.py install
defaults write com.apple.versioner.python Prefer-32-Bit -bool yes 
cd ..

wget http://pypi.python.org/packages/source/s/simplejson/simplejson-2.3.3.tar.gz
gzip -d simplejson*
tar -x -f simplejson-2.3.3.tar
cd simplejson*
sudo python setup.py install
cd ..

wget http://httplib2.googlecode.com/files/httplib2-0.7.4.tar.gz
gzip -d httplib2*
tar -x -f httplib*
cd httplib*
sudo python setup.py install
cd ..

git clone https://github.com/simplegeo/python-oauth2.git
cd python-oath*
sudo python setup.py install
cd ..

wget http://python-twitter.googlecode.com/files/python-twitter-0.8.2.tar.gz
gzip -d python-twitter*
tar -x -f python-twitter*
cd python-twitter*
sudo python setup.py install
cd ..




