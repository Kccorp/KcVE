import os
from cveClass import *
from cpeClass import *


def createFile(path):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <title>KcVE</title>

    <style>
        li{
            background-color: #eeeeee; !important;
        }
    </style>
</head>
<body>
<div class="container mt-5">
    <div class="row">

        <h1 class="mb-5">Cve Report</h1>
        <hr>''')
            f.close()


def appendToFile(path, text):
    file = open(path, 'a')  # Open a file in append mode
    file.write(text)  # Write some text
    file.close()  # Close the file


def createCveReport(cveList, path):
    createFile(path)
    for i in range(len(cveList)):

        # show cve id and cvss infos
        cveReport = '<h2>' + str(cveList[i].id) + '  &nbsp; &nbsp; &nbsp; &nbsp; CVSS version' + str(
            cveList[i].version) + '</h2>'
        cveReport += '<p>Published Date: ' + cveList[i].publishedDate + '<br> lastModifiedDate: ' + cveList[
            i].lastModifiedDate + '</p>'
        cveReport += '<h3>Description</h3><p>' + cveList[i].description + '</p>'
        cveReport += '<h3>CVSS</h3><h4>Base Score: ' + str(cveList[i].baseScore) + '<br>Vector String: ' + cveList[
            i].vectorString + '<br>Exploitability Score: ' + str(cveList[i].exploitabilityScore) + '</p>'

        # show all cpes for a cve object
        cveReport += '<h3>Vulnerable CPEs</h3>'
        for j in range(len(cveList[i].cpeList)):
            cveReport += '<ul class="list-group list-group-horizontal">'
            cveReport += '<li class="list-group-item">vendor:' + cveList[i].cpeList[j].vendor + ' product: ' + \
                         cveList[i].cpeList[j].product + ' version: ' + cveList[i].cpeList[j].version + '</li>'

            if cveList[i].cpeList[j].minVersion is not None and cveList[i].cpeList[j].maxVersion is not None:
                cveReport += '<li class="list-group-item">minVersion:' + cveList[i].cpeList[
                    j].minVersion + ' maxVersion:' + \
                             cveList[i].cpeList[j].maxVersion + '</li>'
            if cveList[i].cpeList[j].minVersion is not None:
                cveReport += '<li class="list-group-item">minVersion:' + cveList[i].cpeList[j].minVersion + '</li>'
            if cveList[i].cpeList[j].maxVersion is not None:
                cveReport += '<li class="list-group-item">maxVersion:' + cveList[i].cpeList[j].maxVersion + '</li>'
            cveReport += '</ul>'

        # show the source and url reference
        cveReport += '<h3 class="mt-3">Source</h3><p>' + cveList[i].source + '</p>'
        cveReport += '<h3>URL Reference</h3><p>' + cveList[i].urlSource + '</p>'

        cveReport += '<hr class="my-4">'

        appendToFile(path, cveReport)
