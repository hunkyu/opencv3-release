Name:           ros-kinetic-opencv3
Version:        3.1.0
Release:        9%{?dist}
Summary:        ROS opencv3 package

Group:          Development/Libraries
License:        BSD
URL:            http://opencvg.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ffmpeg-devel
Requires:       jasper-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       numpy
Requires:       python-devel
Requires:       qt5-qtbase-gui
Requires:       ros-kinetic-catkin
Requires:       vtk-devel
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  ffmpeg-devel
BuildRequires:  jasper-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff
BuildRequires:  libv4l-devel
BuildRequires:  numpy
BuildRequires:  python-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel

%description
OpenCV 3.x

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 07 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-9
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-8
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-7
- Autogenerated by Bloom

* Tue Apr 05 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-6
- Autogenerated by Bloom

* Thu Mar 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-3
- Autogenerated by Bloom

* Thu Mar 17 2016 Vincent Rabaud <vincent.rabaud@gmail.com> - 3.1.0-2
- Autogenerated by Bloom

