### RPM lcg root-toolfile 2.0
Requires: root
%prep

%build

%install

mkdir -p %i/etc/scram.d
# root_interface toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/root_interface.xml
<tool name="root_interface" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <client>
    <environment name="ROOT_INTERFACE_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE"             default="$ROOT_INTERFACE_BASE/include"/>
    <environment name="LIBDIR"              default="$ROOT_INTERFACE_BASE/lib"/>
  </client>
  <runtime name="PATH"       value="$ROOT_INTERFACE_BASE/bin" type="path"/>
  <runtime name="PYTHONPATH" value="$ROOT_INTERFACE_BASE/lib" type="path"/>
  <runtime name="ROOTSYS"    value="$ROOT_INTERFACE_BASE/"/>
</tool>
EOF_TOOLFILE

# rootcint toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootcint.xml
<tool name="rootcint" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Core"/>
  <lib name="Cint"/>
  <client>
    <environment name="ROOTCINT_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE"       default="$ROOTCINT_BASE/cint"/>
  </client>
  <use name="root_interface"/>
  <use name="sockets"/>
  <use name="pcre"/>
  <use name="zlib"/>
</tool>
EOF_TOOLFILE

# rootrint toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootrint.xml
<tool name="rootrint" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Rint"/>
  <use name="rootcint"/>
</tool>
EOF_TOOLFILE

# rootrio toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootrio.xml
<tool name="rootrio" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="RIO"/>
  <use name="rootcint"/>
</tool>
EOF_TOOLFILE

# rootthread toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootthread.xml
<tool name="rootthread" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Thread"/>
  <use name="rootrio"/>
</tool>
EOF_TOOLFILE

# rootxmlio toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootxmlio.xml
<tool name="rootxmlio" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="XMLIO"/>
  <use name="rootrio"/>
</tool>
EOF_TOOLFILE

# rootmathcore toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootmathcore.xml
<tool name="rootmathcore" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="MathCore"/>
  <use name="rootcint"/>
</tool>
EOF_TOOLFILE

# rootcore toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootcore.xml
<tool name="rootcore" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Tree"/>
  <lib name="Net"/>
  <use name="rootmathcore"/>
  <use name="rootthread"/>
</tool>
EOF_TOOLFILE

# roothistmatrix toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/roothistmatrix.xml
<tool name="roothistmatrix" version="@TOOL_VERSION@"> 
  <info url="http://root.cern.ch/root/"/>
  <lib name="Hist"/>
  <lib name="Matrix"/>
  <use name="rootcore"/>
</tool>
EOF_TOOLFILE

# rootspectrum toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootspectrum.xml
<tool name="rootspectrum" version="@TOOL_VERSION@"> 
  <info url="http://root.cern.ch/root/"/>
  <lib name="Spectrum"/>
  <use name="roothistmatrix"/>
</tool>
EOF_TOOLFILE

# rootphysics toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootphysics.xml
<tool name="rootphysics" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Physics"/>
  <use name="roothistmatrix"/>
</tool>
EOF_TOOLFILE

# root toolfile, alias for rootphysics. Using rootphysics is preferred.
cat << \EOF_TOOLFILE >%i/etc/scram.d/root.xml
<tool name="root" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <use name="rootphysics"/>
</tool>
EOF_TOOLFILE

# rootgpad toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootgpad.xml
<tool name="rootgpad" version="@TOOL_VERSION@"> 
  <info url="http://root.cern.ch/root/"/>
  <lib name="Gpad"/>
  <lib name="Graf"/>
  <use name="roothistmatrix"/>
</tool>
EOF_TOOLFILE

# rootgraphics toolfile, identical to old "root" toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootgraphics.xml
<tool name="rootgraphics" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="TreePlayer"/>
  <lib name="Graf3d"/>
  <lib name="Postscript"/>
  <use name="rootgpad"/>
</tool>
EOF_TOOLFILE

# rooteg toolfile, identical to old "root" toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rooteg.xml
<tool name="rooteg" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="EG"/>
  <use name="rootgraphics"/>
</tool>
EOF_TOOLFILE

# rootpy toolfile, identical to old "root" toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootpy.xml
<tool name="rootpy" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="PyROOT"/>
  <use name="rootgraphics"/>
</tool>
EOF_TOOLFILE

# rootinteractive toolfile 
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootinteractive.xml
<tool name="rootinteractive" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Gui"/>
  <use name="libjpg"/>
  <use name="libpng"/>
  <use name="rootgpad"/>
  <use name="rootrint"/>
</tool>
EOF_TOOLFILE

# rootmath toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootmath.xml
<tool name="rootmath" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="GenVector"/>
  <lib name="MathMore"/>
  <use name="rootcore"/>
  <use name="gsl"/>
</tool>
EOF_TOOLFILE

# rootminuit toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootminuit.xml
<tool name="rootminuit" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Minuit"/>
  <use name="rootgpad"/>
</tool>
EOF_TOOLFILE

# rootminuit2 toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootminuit2.xml
<tool name="rootminuit2" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Minuit2"/>
  <use name="rootgpad"/>
</tool>
EOF_TOOLFILE

# rootrflx toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootrflx.xml
<tool name="rootrflx" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Reflex"/>
  <client>
    <environment name="ROOTRFLX_BASE" default="@TOOL_ROOT@"/>
  </client>
  <flags GENREFLEX_GCCXMLOPT="@GENREFLEX_GCCXMLOPT@"/>
  <flags GENREFLEX_CPPFLAGS="-DCMS_DICT_IMPL -D_REENTRANT -DGNUSOURCE -D__STRICT_ANSI__"/>
  <flags GENREFLEX_ARGS="--deep"/>
  <runtime name="GENREFLEX" value="$ROOTRFLX_BASE/bin/genreflex"/>
  <use name="gccxml"/>
  <use name="root_interface"/>
</tool>
EOF_TOOLFILE

# roothtml toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/roothtml.xml
<tool name="roothtml" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Html"/>
  <use name="rootgpad"/>
</tool>
EOF_TOOLFILE

# rootmlp toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootmlp.xml
<tool name="rootmlp" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="MLP"/>
  <use name="rootgraphics"/>
</tool>
EOF_TOOLFILE

# roottmva toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/roottmva.xml
<tool name="roottmva" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="TMVA"/>
  <use name="rootmlp"/>
  <use name="rootminuit"/>
</tool>
EOF_TOOLFILE

# rootxml toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootxml.xml
<tool name="rootxml" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="XMLParser"/>
  <use name="rootcore"/>
  <use name="libxml2"/>
</tool>
EOF_TOOLFILE

# rootfoam toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootfoam.xml
<tool name="rootfoam" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Foam"/>
  <use name="roothistmatrix"/>
</tool>
EOF_TOOLFILE

# rootcintex toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootcintex.xml
<tool name="rootcintex" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Cintex"/>
  <use name="rootrflx"/>
  <use name="rootcint"/>
</tool>
EOF_TOOLFILE

# rootgeom toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootgeom.xml
<tool name="rootgeom" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Geom"/>
  <use name="rootrio"/>
  <use name="rootmathcore"/>
</tool>
EOF_TOOLFILE

# rootgeompainter toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootgeompainter.xml
<tool name="rootgeompainter" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="GeomPainter"/>
  <use name="rootgeom"/>
  <use name="rootgraphics"/>
</tool>
EOF_TOOLFILE

# rootrgl toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootrgl.xml
<tool name="rootrgl" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="RGL"/>
  <use name="rootinteractive"/>
  <use name="rootgraphics"/>
</tool>
EOF_TOOLFILE

# rooteve toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rooteve.xml
<tool name="rooteve" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="Eve"/>
  <use name="rootgeompainter"/>
  <use name="rootrgl"/>
</tool>
EOF_TOOLFILE

# rootguihtml toolfile
cat << \EOF_TOOLFILE >%i/etc/scram.d/rootguihtml.xml
<tool name="rootguihtml" version="@TOOL_VERSION@">
  <info url="http://root.cern.ch/root/"/>
  <lib name="GuiHtml"/>
  <use name="rootinteractive"/>
</tool>
EOF_TOOLFILE

case %cmsos in
  *_ia32)
    GENREFLEX_GCCXMLOPT="-m32"
  ;;
  *_amd64)
    GENREFLEX_GCCXMLOPT="-m64"
  ;;
esac
export GENREFLEX_GCCXMLOPT

## IMPORT scram-tools-post
