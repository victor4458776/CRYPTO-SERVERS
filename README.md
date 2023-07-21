# Cryptography
Cryptographic systems for web-robot automation with python

# Code snipets
This project is useful for python programmers to automate web tasks with important cryptographic libraries in python
# Composition

AUTOMATE-SOCKETS
HTTPLIB3
REQUEST-LIBRARY
XML-web scraping
x509 certificates (Documentation)
crypto-chains (money transactions)

The crypto project is based on solid knowledge in the cybersecurity field with some useful
practical and projective ideas to develop the basic structure of the web server in the backend
for the python programming field.

This is the exact location where the certificates are placed in sytems for computer users;
/etc $ nano hosts
/etc $ nano permissions
/etc $ cd security
/etc/security $ ls
cacerts  cacerts_wfa  otacerts.zip
/etc/security $ cd cacerts
.../security/cacerts $ ls
00673b5b.0  1df5a75f.0  2d9dafe4.0  3c58f906.0  4e18c148.0  5f47b495.0  7999be0d.0  882de061.0  9685a493.0  a7d2cf64.0  b936d1c6.0  cb156124.0  d59297b8.0  e8651083.0
02756ea4.0  1e1eab7c.0  2fa87019.0  3c6676aa.0  5046c355.0  60afe812.0  7a7c655d.0  88950faa.0  9772ca32.0  a81e292b.0  bc3f2570.0  cb1c3204.0  d6e6eab9.0  ed39abd0.0
04f60c28.0  1e8e7201.0  31188b5e.0  3c860d51.0  524d9b43.0  6187b673.0  7a819ef2.0  89c02a45.0  9c3323d4.0  ab5346f4.0  bdacca6f.0  ccc52f49.0  d7746a63.0  ee7cd6fb.0
0d5a4e1c.0  1eb37bdf.0  33ee480d.0  3c9a4d3b.0  52b525c7.0  63a2c897.0  7c302982.0  8d6437c3.0  9d6523ce.0  ab59055e.0  bf64f35b.0  cf701eeb.0  d8317ada.0  facacbc6.0
0d69c7e1.0  1f58a078.0  343eb6cb.0  3d441de8.0  559f7c71.0  67495436.0  7d453d8f.0  91739615.0  9dbefe7b.0  aeb67534.0  c2c1704e.0  d06393bb.0  dbc54cab.0  fb5fa911.0
10531352.0  21855f49.0  35105088.0  3e7271e8.0  583d0756.0  69105f4f.0  81b9768f.0  9282e51c.0  9f533518.0  b0ed035a.0  c491639e.0  d0cddf45.0  dc99f41e.0  fd08c599.0
111e6273.0  219d9499.0  3929ec9f.0  40dc992e.0  5a250ea7.0  6fcc125d.0  82223c44.0  9339512a.0  a0bc6fbb.0  b0f3e76e.0  c51c224c.0  d16a5865.0  dfc0fe80.0  fde84897.0
12d55845.0  23f4c490.0  399e7759.0  455f1b52.0  5a3f0ff8.0  75680d2e.0  85cde254.0  9479c8c3.0  a2c66da8.0  b3fb433b.0  c7e2a638.0  d18e9066.0  e442e424.0
17b51fe6.0  27af790d.0  3a3b02ce.0  48a195d8.0  5cf9d536.0  76579174.0  86212b19.0  9576d26b.0  a3896b44.0  b7db1890.0  c907e29b.0  d41b5e2a.0  e48193cf.0
1dcd6f4c.0  2add47b6.0  3ad48a91.0  4be590e0.0  5e4e69e7.0  7892ad52.0  87753b0d.0  95aff9e3.0  a7605362.0  b872f2b4.0  c90bc37d.0  d4c339cb.0  e775ed2d.0
.../security/cacerts $ nano 2d9dafe4.0

Download a valid google certitificate
(Hacking SSL certificates throghout programming in code)

require 'open-uri'
=> true
irb(main):003:2* def validate_https_cert(target) begin
irb(main):004:2*     open("https://#{target}")
irb(main):005:2*     puts '[+] Valid Certificate'
irb(main):006:2* rescue OpenSSL::SSL::SSLError
irb(main):007:2*   puts '[+] Invalid SSL Certificate'
irb(main):008:1* end
irb(main):009:0> end
=> :validate_https_cert
irb(main):010:0> valid_ssl = 'google.com'
=> "google.com"
irb(main):011:0> nonvalid_cerificate = 'expired.badssl.com'
=> "expired.badssl.com"
irb(main):012:0> validate_https_cert valid_ssl
(irb):6:in `rescue in validate_https_cert': uninitialized constant OpenSSL (NameError)
        from (irb):3:in `validate_https_cert'
        from (irb):12:in `<main>'
        from /data/data/com.termux/files/usr/lib/ruby/gems/3.2.0/gems/irb-1.6.2/exe/irb:11:in `<top (required)>'


#See that we need to choose a target to begin with. Also we need to rescue some classes in a directory format like OpenSSL/SSL/SSLError
to check load errors see the print functions in the Invalid SSL Certificate
and the process to validate the certificate is in the => :validate_https_cert and the two variables to analyze download errors are:
valid_ssl = 'google.com' and the nonvalid_certificate = 'expired.badssl.com'




