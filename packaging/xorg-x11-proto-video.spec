Name:     xorg-x11-proto-video
Summary:  X.Org X11 Protocol videoproto
Version:  2.3.2
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.gz
Provides: videoproto

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

# some file to be intalled can be ignored when rpm generates packages
%define _unpackaged_files_terminate_build 0

%description
Description: %{summary}
This extension provides a protocol for a video output mechanism,
mainly to rescale video playback in the video controller hardware.

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
