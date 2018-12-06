#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI-Escape-XS
Version  : 0.14
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/URI-Escape-XS-0.14.tar.gz
Summary  : 'Drop-In replacement for URI::Escape'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-URI-Escape-XS-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
URI::Escape::XS - Drop-In replacement for URI::Escape
VERSION
SYNOPSIS
# use it instead of URI::Escape
use URI::Escape::XS qw/uri_escape uri_unescape/;
$safe = uri_escape("10% is enough\n");
$verysafe = uri_escape("foo", "\0-\377");
$str  = uri_unescape($safe);

%package dev
Summary: dev components for the perl-URI-Escape-XS package.
Group: Development
Requires: perl-URI-Escape-XS-lib = %{version}-%{release}
Provides: perl-URI-Escape-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-URI-Escape-XS package.


%package lib
Summary: lib components for the perl-URI-Escape-XS package.
Group: Libraries

%description lib
lib components for the perl-URI-Escape-XS package.


%prep
%setup -q -n URI-Escape-XS-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/URI/Escape/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI::Escape::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/URI/Escape/XS/XS.so
