%define		fversion	%(echo %{version} |tr r -)
%define		modulename	sma
Summary:	Statistical Microarray Analysis
Summary(pl.UTF-8):	Statystyczne analizy mikrotablicowe
Name:		R-cran-%{modulename}
Version:	0.5.14
Release:	2
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	b669496897c520eb0a78ff62c647f3ef
URL:		http://www.stat.berkeley.edu/users/terry/zarray/Html/smacode.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package contains some simple functions for exploratory microarray
analysis.

%description -l pl.UTF-8
Pakiet zawiera proste funkcje do wstępnej analizy mikrotablicowej.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
