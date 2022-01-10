# Step1: Start new screen and become root user
screen
sudo su
yum update -y
# Step2: Install python3 ,pip,Git and virtualenv
yum install python3 -y
yum install pip
pip install virtualenv
# Step3: Create virtual environment with python3 and activate that environment
virtualenv -p python3.7 my_app
source ./my_app/bin/activate
# Step4: Install chrome webdriver
cd /tmp/
wget https://chromedriver.storage.googleapis.com/97.0.4692.20/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
chromedriver --version
# Step5: Install chrome browser
curl https://intoli.com/install-google-chrome.sh | bash
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version && which google-chrome
# Step6: Install necessary python libraries
pip3 install selenium