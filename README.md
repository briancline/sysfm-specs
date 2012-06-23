# sys.fm RPM SPEC file sources

This repo contains the original SPEC files and other patch and configuration
files required to build the RPMS currently available at the http://rpm.sys.fm/ 
repository.


# Using rpm.sys.fm

To begin using packages provided from rpm.sys.fm, run the following command to install the yum repository configuration. It will be enabled in yum right away.

`rpm -Uvh http://rpm.sys.fm/centos/6/noarch/sysfm-release-6-1.el6.noarch.rpm`


# Packages

The following packages are currently provided:

```
cloudfuse          Use Rackspace Cloud Files (or any Swift install) as a mountpoint.
double-conversion  Google's double-conversion library, extracted from V8.
fb303              Facebook Bassline (via Thrift's latest contrib sources).
fb303-0.5.0        Facebook Bassline from Thrift 0.5.0 (best for Scribe).
gflags             Google's gflags library.
google-glog        Google's glog library.
php-proctitle      The PECL proctitle extension, allowing process names to be set.
phpredis           A native PHP extension for Redis, including a session handler.
redis              Redis key-value store (latest release).
scribe             Facebook Scribe, a distributed logging service/aggregator.
sysfm-release      Provides the repo file for using rpm.sys.fm packages via yum.
thrift             Apache Thrift (latest release).
thrift-0.5.0       Apache Thrift v0.5.0 (best for Scribe).
```


# Credits

Much of the countless days and hours spent compiling thrift, fb303, and scribe 
on Enterprise Linux 6 were severely reduced and much hair was saved by the 
SPEC files provided by Silas Sewell at https://github.com/silas/rpms.

Should you find yourself wishing and praying for any particular package on any 
enterprise linux distribution, you might check his repo first.

* Silas Sewell's spec files: https://github.com/silas/rpms
* The official spec file from thrift: https://github.com/apache/thrift/blob/trunk/contrib/thrift.spec
* The redis spec file from FC EPEL6: http://pkgs.fedoraproject.org/gitweb/?p=redis.git;a=tree
* The spec file written and submitted for cloudfuse by kynx@github: https://gist.github.com/2960984/30c3632df89acd1a6c68b5330839e754965a8bf8
* Google's own spec files for double-conversion, glog, and gflags
* Facebook's patch to use the double-conversion code as a standalone system library: https://github.com/facebook/folly/blob/master/folly/SConstruct.double-conversion

***

# License (BSD)

Copyright (c) 2012, Brian Cline
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
