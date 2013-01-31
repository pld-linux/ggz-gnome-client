Summary:	GNOME core client for GGZ
Summary(pl.UTF-8):	Klient GGZ dla środowiska GNOME
Name:		ggz-gnome-client
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6e9da98c7b519edd39937b0641c46800
URL:		http://www.ggzgamingzone.org/
BuildRequires:	gettext-devel
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	pkgconfig
Requires:	ggz-client-libs-devel >= 0.0.14
Requires:	libggz-devel >= 0.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNOME core client for GGZ.

%description -l pl.UTF-8
Ten pakiet to klient GGZ dla środowiska GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.GGZ
%attr(755,root,root) %{_bindir}/ggz-gnome
%attr(755,root,root) %{_bindir}/motd_editor
%{_datadir}/ggz/ggz-gnome
%{_mandir}/man6/ggz-gnome.6*
%{_mandir}/man6/motd_editor.6*
