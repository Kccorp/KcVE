# KcVE
KcVE is a comprehensive CVE (Common Vulnerabilities and Exposures) tool that allows users to gather and parse information about the latest vulnerabilities from publicly available sources. It features are easy-to-use that allows users to access informations with just a few clicks. 

The app exports the information in an HTML format, making it easy to share and analyze. This tool is ideal for security professionals, researchers, and others who need to stay informed about the latest vulnerabilities and ensure the security of their systems. 

With KcVE, users can access the latest information about CVEs quickly and efficiently, giving them the ability to take action to protect their systems and data.

## Prerequisites
Before installing KcVE, you will need to make sure you have the following dependencies installed:

```bash
>= python 3.10
>= pip 22.3.1
```
## Installation

### Option 1: install from source
To install KcVE, you can use the following command:

```bash
git clone https://github.com/Kccorp/KcVE.git
cd KcVE
pip install -r requirements.txt
```

### Option 2: install from DockerHub

## Usage

### Option 1: run from source

```bash
python main.py [-h] [-k KEYWORD] -s STARTDATE -e ENDDATE [-v VENDOR] [-p PRODUCT] [-w OUTPUT]

```

### Option 2: run from DockerHub

```bash
docker run -it --rm kccorp/kcve
```

### Example

```bash
python main.py -s "2023-01-01" -e "2023-02-01" -v "fortinet" -p "fortios" -w "fortios.html"
```

### Help

```bash
CVE Search

options:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        Keyword to search for
  -s STARTDATE, --startDate STARTDATE
                        Start date to search for
  -e ENDDATE, --endDate ENDDATE
                        End date to search for
  -v VENDOR, --vendor VENDOR
                        Vendor to search for
  -p PRODUCT, --product PRODUCT
                        Product to search for
  -w OUTPUT, --output OUTPUT
                        Output file name
```


## Ressources

### API

https://services.nvd.nist.gov/rest/json/cves/2.0

### NIST (documentation)

https://nvd.nist.gov/developers/vulnerabilities

## Authors

- [@Keissy](https://www.github.com/kccorp)


