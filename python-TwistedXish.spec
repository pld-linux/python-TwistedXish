%define 	module	TwistedXish

Summary:	XML library for Twisted
Summary(pl.UTF-8):	Biblioteka XML dla Twisted
Name:		python-%{module}
Version:	0.1.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Xish/0.1/%{module}-%{version}.tar.bz2
# Source0-md5:	7b1f88640517a6bf3524ddab279996f4
URL:		http://twistedmatrix.com/projects/xish/
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted X-ish is a library for processing XML with Twisted and Python,
with support for a Pythonic DOM and an XPath-like toolkit. It exists
largely to facilitate the Jabber support in Twisted Words.

%description -l pl.UTF-8
Twisted X-ish to biblioteka do przetwarzania XML-a przy użyciu Twisted
i Pythona z obsługą Pythonic DOM i toolkitem w stylu XPath. Istnieje
przede wszystkim dla łatwiejszej obsługi Jabbera w Twisted Words.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/twisted/xish
