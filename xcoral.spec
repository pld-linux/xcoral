Summary:	Xcoral Editor
Summary(pl):	Xcoral - edytor tekstów pracuj±cy w ¶rodowisku X
Name:		xcoral
Version:	3.2
Release:	6
License:	GPL
Group:		X11/Applications/Editors
Source0:	ftp://ftp.x.org/contrib/editors/%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
Patch1:		%{name}-loop.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Xcoral is a multiwindow mouse-based text editor for the XWindow
System. A built-in browser enables you to navigate through C
functions, C++ classes, methods and files.

%description -l pl
Xcoral to wielookienkowy tekstowy edytor bazuj±cy na obs³udze myszki.
Posiada wbudowane mechanizmy pozwalaj±ce w sposób wyra¼ny rozgraniczyæ
tworzony tekst.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_13

%{__make} XC_LIBDIR=%{_datadir}/%{name}

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
%doc Doc/HTML IAFA-PACKAGE
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
