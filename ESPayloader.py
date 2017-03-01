#!/usr/bin/env python
""" Simple Elastic Search Sender """

import json
from optparse import OptionParser
from elasticsearch import Elasticsearch


def main():
    """ Main function"""
    parser = OptionParser()

    parser.add_option("-a", "--address", dest="address", help="ElasticSearch Address")
    parser.add_option("-i", "--index", dest="index", help="ElasticSearch Index")
    parser.add_option("-d", "--docType", dest="docType", help="ElasticSearch DocType")
    parser.add_option("-p", "--payload", dest="payload", help="Json Data Payload")

    (options, args) = parser.parse_args()

    if options.address is None:
        parser.error('Elasticsearch address required. [http://address:port]')

    if options.index is None:
        parser.error('Elasticsearch Index required.')

    if options.docType is None:
        parser.error('Elasticsearch docType required.')

    if options.payload is None:
        parser.error('Json data payload required')
        

    indexer(options.address, options.index, options.payload, options.docType)

def indexer(url, index, payload, doc_type):
    """ Send to elasticsearch """
    els = Elasticsearch([url])
    els.index(index=index, doc_type=doc_type, body=json.loads(payload))
    print "Data indexed sucessfully."

main()
