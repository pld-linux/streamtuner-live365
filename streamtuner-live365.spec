Summary:	Live365 plugin for streamtuner
Summary(pl):	Wtyczka Live365 dla streamtunera
Name:		streamtuner-live365
Version:	0.3.4
Release:	1
License:	Free
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/streamtuner/%{name}-%{version}.tar.gz
# Source0-md5:	6ec15ca72fdbe9c5e6acc30757a4b6c7
URL:		http://www.nongnu.org/streamtuner/
Buildrequires:	gtk+2-devel >= 2:2.4.4
Buildrequires:	streamtuner-devel >= 0.12.0
Requires:	streamtuner >= 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Live365 plugin for streamtuner.

%description -l pl
Wtyczka Live365 dla streamtunera.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/streamtuner/plugins/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/streamtuner/plugins/*.so
