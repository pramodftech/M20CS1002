from . import hjbf,dbf,abbf
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime
from urllib.parse import urlparse,urlencode

#Function to extract features
def featureExtraction(url,label):

  features = []
  #Address bar based features (10)
  features.append(abbf.getDomain(url))
  features.append(abbf.havingIP(url))
  features.append(abbf.haveAtSign(url))
  features.append(abbf.getLength(url))
  features.append(abbf.getDepth(url))
  features.append(abbf.redirection(url))
  features.append(abbf.httpDomain(url))
  features.append(abbf.tinyURL(url))
  features.append(abbf.prefixSuffix(url))
  
  #Domain based features (4)
  dns = 0
  try:
    domain_name = whois.whois(urlparse(url).netloc)
  except:
    dns = 1

  features.append(dns)
  features.append(dbf.web_traffic(url))
  features.append(1 if dns == 1 else dbf.domainAge(domain_name))
  features.append(1 if dns == 1 else dbf.domainEnd(domain_name))
  
  # HTML & Javascript based features (4)
  try:
    response = hjbf.requests.get(url)
  except:
    response = ""
  features.append(hjbf.iframe(response))
  features.append(hjbf.mouseOver(response))
  features.append(hjbf.rightClick(response))
  features.append(hjbf.forwarding(response))
  
  
  return features