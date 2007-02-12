Summary:	Xcoral Editor
Summary(pl.UTF-8):   Xcoral - edytor tekstów pracujący w środowisku X
Name:		xcoral
Version:	3.42b
Release:	2
License:	GPL
Group:		X11/Applications/Editors
#Source0Download: http://xcoral.free.fr/download.html
Source0:	http://xcoral.free.fr/%{name}-%{version}.tar.gz
# Source0-md5:	070249fb6ba8eb37014a78d487d7e517
Patch0:		%{name}-misc.patch
URL:		http://xcoral.free.fr/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xcoral is a multiwindow mouse-based text editor for the XWindow
System. A built-in browser enables you to navigate through C
functions, C++ classes, methods and files.

%description -l pl.UTF-8
Xcoral to wielookienkowy tekstowy edytor bazujący na obsłudze myszki.
Posiada wbudowane mechanizmy pozwalające w sposób wyraźny rozgraniczyć
tworzony tekst.

%prep
%setup -q
%patch0 -p0

%build
%configure2_13

%{__make} \
	XC_LIBDIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

%{__make} install \
	installprefix=$RPM_BUILD_ROOT \
	XC_LIBDIR=%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/*.ps IAFA-PACKAGE
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
