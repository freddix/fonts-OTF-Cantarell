Summary:	Cantarell fonts
Name:		fonts-OTF-Cantarell
Version:	0.0.16
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/0.0/cantarell-fonts-%{version}.tar.xz
# Source0-md5:	6665af844817ec1390f8ae2a16feb369
URL:		http://abattis.org/cantarell/
Requires(post,postun):	fontpostinst
Requires:	fontconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
Cantarell is a set of fonts designed by Dave Crossland. It is a
sans-serif Humanist typeface family.

%prep
%setup -qn cantarell-fonts-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

cp -a otf/*.otf $RPM_BUILD_ROOT%{otffontsdir}
cp fontconfig/31-cantarell.conf $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail
ln -s %{_datadir}/fontconfig/conf.avail/31-cantarell.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%{_datadir}/fontconfig/conf.avail/31-cantarell.conf
%{_sysconfdir}/fonts/conf.d/31-cantarell.conf
%{otffontsdir}/Cantarell-*.otf

