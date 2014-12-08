class config():
    def __init__(self):
        self.replica_map = {
                "us-east" : ("54.174.6.90", "N. Virginia",(35.53,-77.43)),
                "us-west" : ("54.149.9.25", "Orgeon", (47.6097, -122.3331)),
                "us-cali" : ("54.67.86.61", "N. California", (38.5556, -121.46889)),
                "gb" : ("54.72.167.104", "Ireland",(53.3331, -6.2489)),
                "de" : ("54.93.182.67", "Frankfurt, Germany", (50.1167, 8.6833)),
                "sg" : ("54.169.146.226", "Singapore", (1.2931, 103.8558)),
                "jp" : ("54.65.104.220", "Tokyo, Japan", (35.69, 139.69)),
                "au" : ("54.66.212.131", "Syndey, Australia", (-33.8615, 151.2055)),
                "br" : ("54.94.156.232", "Sao Paulo, Brazil", (-23.5500, -46.6333))
        }
        self.origin_port = 8080
        self.port = None
        self.name = None
        self.origin = "ec2-54-164-51-70.compute-1.amazonaws.com"
        self.cdn = "cs5700cdnproject.ccs.neu.edu"
