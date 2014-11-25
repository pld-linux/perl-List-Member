#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	List
%define		pnam	Member
%include	/usr/lib/rpm/macros.perl
Summary:	List::Member - PROLOG's member/2: return index of $x in @y
Summary(pl.UTF-8):	List::Member - member/2 z PROLOGa: zwraca indeks $x w @y
Name:		perl-List-Member
Version:	0.044
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/L/LG/LGODDARD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b75ecfec47a907e05dd3daab108da9fc
URL:		http://search.cpan.org/dist/List-Member/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny routine to achieve the same effect as PROLOG's "member/2".

Returns the index of supplied scalar in supplied array, or returns the
value of the package's "$NEG" scalar. This can be over-riden for the
case when the target is the same as the default "-1".

%description -l pl.UTF-8
Jest to mała funkcja napisana tak, by dawać taki sam efekt jak
"member/2" z PROLOGa. Zwraca indeks podanej liczby w podanej tablicy
lub zwraca wartość liczby "$NEG" z pakietu. Ta liczba może być
nadpisana na wypadek, gdyby poszukiwana liczba była taka sama, jak
domyślna $NEG, czyli -1.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
