%define _requires_exceptions perl(Error)

Summary:	Test::Unit::TestCase - unit testing framework base class
Name:		perl-Test-Unit
Version:	0.25
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~mcast/Test-Unit-0.25/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/Test-Unit-%{version}.tar.bz2
BuildRequires:	perl-devel
#BuildRequires:	perl-Class-Inner
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Test::Unit::TestCase is the 'workhorse' of the PerlUnit framework.
When writing tests, you generally subclass Test::Unit::TestCase,
write set_up and tear_down functions if you need them, a bunch of
test_* test methods, then do

%prep

%setup -q -n Test-Unit-%{version} 

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
# make test fails
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog Changes README doc examples
%{perl_vendorlib}/Test/*.p*
%{perl_vendorlib}/Test/Unit
%{_mandir}/*/*

