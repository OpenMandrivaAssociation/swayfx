Name: swayfx
Version: 0.5.3
Release: 1
Summary: A Beautiful Sway Fork
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/WillPower3309/swayfx
Source0:  https://github.com/WillPower3309/swayfx/archive/%{version}/%{name}-%{version}.tar.gz

Conflicts: sway

BuildRequires: meson
BuildRequires: a2x
BuildRequires: pkgconfig(pam)
#BuildRequires: pkgconfig(basu)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wlroots-0.19)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(scenefx-0.4)
BuildRequires: scdoc

%description
Sway is an incredible window manager, and certainly one of the most well established wayland window managers. 
However, it is restricted to only include the functionality that existed in i3. This fork ditches the simple wlr_renderer, and replaces it with our fx_renderer, capable of rendering with fancy GLES2 effects. This, along with a couple of minor changes, expands sway's featureset to include the following:

- Blur
- Anti-aliased rounded corners, borders, and titlebars
- Shadows
- Dim unfocused windows
- Scratchpad treated as minimize: Allows docks, or panels with a taskbar, to correctly interpret minimize / unminimize requests (thanks to LCBCrion) nixify the repo: 
  Allows nixos users to easily contribute to and test this project

%prep
%autosetup -p1

%build
%meson \
	-Dwerror=false
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_sysconfdir/%name/config.d

%files
%doc README.md
%config(noreplace) %_sysconfdir/sway/config
%_bindir/sway
%_bindir/swaybar
%_bindir/swaymsg
%_bindir/swaynag
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_datadir/wayland-sessions/sway.desktop
%dir %_sysconfdir/sway
%_datadir/bash-completion/completions/sway*
%_datadir/fish/vendor_completions.d/sway*.fish
%_datadir/zsh/site-functions/_sway*
%dir %_datadir/backgrounds/sway
%_datadir/backgrounds/sway/*
