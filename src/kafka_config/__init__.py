
import os

# Cloud api details
API_KEY = "5YCGU43L5J4NXDNY" #os.getenv('API_KEY',None)
API_SECRET_KEY = "MGR3Angl7vVaA7ojFLmf7RlPBQnJGal/gdpP+t4UR6qrr545iKBinuh7HsLIflwc" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# Authentication related variables
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

# Schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-10wgj.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "SSSALNXMCVW5JY43" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "re7qwus0P/B2Y8QhbR7t0sm5ZxFfcgIsUHlpkFkMXxu8x5UxgMyQ+yINwlahwSdT" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

