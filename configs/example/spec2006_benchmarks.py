import m5
from m5.objects import *
import os

# These three directory paths are not currently used.
#gem5_dir = '<FULL_PATH_TO_YOUR_GEM5_INSTALL>'
#spec_dir = '<FULL_PATH_TO_YOUR_SPEC_CPU2006_INSTALL>'
#out_dir = '<FULL_PATH_TO_DESIRED_OUTPUT_DIRECTORY>'

config_path = os.path.dirname(os.path.abspath(__file__))
config_root = os.path.dirname(config_path)
m5_root = os.path.dirname(config_root)
out_dir = os.path.join(m5_root, m5.options.outdir) + '/'
cpu2006_dir = '/home/wangzicong/SPEC2006/benchspec/CPU2006/'

alpha_suffix = '_base.i386-m32-gcc42-nn'
#temp
#binary_dir = spec_dir
#data_dir = spec_dir

#400.perlbench
perlbench_run_dir = cpu2006_dir + \
        '400.perlbench/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Perlbench(Process):
    executable = perlbench_run_dir + 'perlbench' + alpha_suffix
    cwd = perlbench_run_dir
    cmd = [executable] + ['-I.', '-I./lib', 'attrs.pl']
    output = out_dir + 'perlbench.out'
    errout = out_dir + 'perlbench.err'

#401.bzip2
bzip2_run_dir = cpu2006_dir + \
        '401.bzip2/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Bzip2(Process):
    executable = bzip2_run_dir + 'bzip2' + alpha_suffix
    cmd = [executable] + ['input.program', '1']
    cwd = bzip2_run_dir
    output = out_dir + 'bzip2.out'
    errout = out_dir + 'bzip2.err'

# TEST CMDS
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'input.program', '1']
# REF CMDS
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'input.source', '280']
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'chicken.jpg', '30']
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'liberty.jpg', '30']
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'input.program', '280']
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'text.html', '280']
#bzip2.cmd = [bzip2.executable] + [bzip2_run_dir + 'input.combined', '200']
#bzip2.output = out_dir + 'bzip2.out'
#bzip2.errout = out_dir + 'bzip2.err'

#403.gcc
gcc_run_dir = cpu2006_dir + '403.gcc/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Gcc(Process):
    executable = gcc_run_dir + 'gcc' + alpha_suffix
    cmd = [executable] + ['cccp.i', '-o', 'cccp.s']
    cwd = gcc_run_dir
    output = out_dir + 'gcc.out'
    errout = out_dir + 'gcc.err'

#410.bwaves
bwaves_run_dir = cpu2006_dir + \
        '410.bwaves/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Bwaves(Process):
    executable = bwaves_run_dir + 'bwaves' + alpha_suffix
    cmd = [executable]
    cwd = bwaves_run_dir
    output = out_dir + 'bwaves.out'
    errout = out_dir + 'bwaves.err'

# TEST CMDS
#bwaves.cmd = [bwaves.executable]
# REF CMDS
#bwaves.cmd = [bwaves.executable]
#bwaves.output = out_dir + 'bwaves.out'
#bwaves.errout = out_dir + 'bwaves.err'

#416.gamess
gamess_run_dir = cpu2006_dir + \
        '416.gamess/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Gamess(Process):
    executable = gamess_run_dir + 'gamess' + alpha_suffix
    cmd = [executable]
    cwd = gamess_run_dir
    input = gamess_run_dir + 'exam29.config'
    output = out_dir + 'gamess.out'
    errout = out_dir + 'gamess.err'

# TEST CMDS
#gamess.cmd = [gamess.executable]
#gamess.input = 'exam29.config'
# REF CMDS
#gamess.cmd = [gamess.executable]
#gamess.input = 'cytosine.2.config'
#gamess.cmd = [gamess.executable]
#gamess.input = 'h2ocu2+.gradient.config'
#gamess.cmd = [gamess.executable]
#gamess.input = 'triazolium.config'
#gamess.output = out_dir + 'gamess.out'
#gamess.errout = out_dir + 'gamess.err'

#429.mcf
mcf_run_dir = cpu2006_dir + '429.mcf/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Mcf(Process):
    executable = mcf_run_dir + 'mcf' + alpha_suffix
    cmd = [executable] + ['inp.in']
    cwd = mcf_run_dir
    output = out_dir + 'mcf.out'
    errout = out_dir + 'mcf.err'

# TEST CMDS
#mcf.cmd = [mcf.executable] + [mcf_run_dir + 'inp.in']
# REF CMDS
#mcf.cmd = [mcf.executable] + [mcf_run_dir + 'inp.in']
#mcf.output = out_dir + 'mcf.out'
#mcf.errout = out_dir + 'mcf.err'

#433.milc
milc_run_dir = cpu2006_dir + \
        '433.milc/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Milc(Process):
    executable = milc_run_dir + 'milc' + alpha_suffix
    cmd = [executable]
    cwd = milc_run_dir
    input = milc_run_dir + 'su3imp.in'
    output = out_dir + 'milc.out'
    errout = out_dir + 'milc.err'

# TEST CMDS
#milc.cmd = [milc.executable]
#milc.input = 'su3imp.in'
# REF CMDS
#milc.cmd = [milc.executable]
#milc.input = 'su3imp.in'
#milc.output = out_dir + 'milc.out'
#milc.errout = out_dir + 'milc.err'

#434.zeusmp
zeusmp_run_dir = cpu2006_dir + \
        '434.zeusmp/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Zeusmp(Process):
    executable = zeusmp_run_dir + 'zeusmp' + alpha_suffix
    cmd = [executable]
    cwd = zeusmp_run_dir
    output = out_dir + 'zeusmp.out'
    errout = out_dir + 'zeusmp.err'

# TEST CMDS
#zeusmp.cmd = [zeusmp.executable]
# REF CMDS
#zeusmp.cmd = [zeusmp.executable]
#zeusmp.output = out_dir + 'zeusmp.out'
#zeusmp.errout = out_dir + 'zeusmp.err'

#435.gromacs
gromacs_run_dir = cpu2006_dir + \
        '435.gromacs/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Gromacs(Process):
    executable = gromacs_run_dir + 'gromacs' + alpha_suffix
    cmd = [executable] + ['-silent','-deffnm', 'gromacs', '-nice','0']
    cwd = gromacs_run_dir
    output = out_dir + 'gromacs.out'
    errout = out_dir + 'gromacs.err'

#436.cactusADM
cactusADM_run_dir = cpu2006_dir + \
        '436.cactusADM/run/run_base_test_i386-m32-gcc42-nn.0000/'
class CactusADM(Process):
    executable = cactusADM_run_dir + 'cactusADM' + alpha_suffix
    cmd = [executable] + [cactusADM_run_dir + 'benchADM.par']
    cwd = cactusADM_run_dir
    output = out_dir + 'cactusADM.out'
    errout = out_dir + 'cactusADM.err'

#437.leslie3d
leslie3d_run_dir = cpu2006_dir + \
        '437.leslie3d/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Leslie3d(Process):
    executable = leslie3d_run_dir + 'leslie3d' + alpha_suffix
    cmd = [executable]
    cwd = leslie3d_run_dir
    input = leslie3d_run_dir + 'leslie3d.in'
    output = out_dir + 'leslie3d.out'
    errout = out_dir + 'leslie3d.err'

# TEST CMDS
#leslie3d.cmd = [leslie3d.executable]
#leslie3d.input = 'leslie3d.in'
# REF CMDS
#leslie3d.cmd = [leslie3d.executable]
#leslie3d.input = 'leslie3d.in'
#leslie3d.output = out_dir + 'leslie3d.out'
#leslie3d.errout = out_dir + 'leslie3d.err'

#444.namd
namd_run_dir = cpu2006_dir + \
        '444.namd/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Namd(Process):
    executable = namd_run_dir + 'namd' + alpha_suffix
    cmd = [executable] + ['--input', 'namd.input', '--output', 'namd.out',
            '--iterations', '1']
    cwd = namd_run_dir
    output = out_dir + 'namd.out'
    errout = out_dir + 'namd.err'

#445.gobmk
gobmk_run_dir = cpu2006_dir + \
        '445.gobmk/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Gobmk(Process):
    executable = gobmk_run_dir + 'gobmk' + alpha_suffix
    cmd = [executable] + ['--quiet','--mode', 'gtp']
    cwd = gobmk_run_dir
    input = gobmk_run_dir + 'dniwog.tst'
    output = out_dir + 'gobmk.out'
    errout = out_dir + 'gobmk.err'


# TEST CMDS
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'dniwog.tst'
# REF CMDS
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = '13x13.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'nngs.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'score2.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'trevorc.tst'
#gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
#gobmk.input = 'trevord.tst'
#gobmk.output = out_dir + 'gobmk.out'
#gobmk.errout = out_dir + 'gobmk.err'

#447.dealII
dealII_run_dir = cpu2006_dir + \
        '447.dealII/run/run_base_test_i386-m32-gcc42-nn.0000/'
dealII=Process()
dealII.executable = dealII_run_dir + 'dealII' + alpha_suffix
####### NOT WORKING #########

# TEST CMDS
####### NOT WORKING #########
#dealII.cmd = [gobmk.executable]+['8']
# REF CMDS
####### NOT WORKING #########
dealII.output = out_dir + 'dealII.out'
dealII.errout = out_dir + 'dealII.err'

#450.soplex
soplex_run_dir = cpu2006_dir + \
        '450.soplex/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Soplex(Process):
    executable = soplex_run_dir + 'soplex' + alpha_suffix
    cmd = [executable] + ['-m10000', soplex_run_dir + 'test.mps']
    cwd = out_dir
    output = out_dir + 'soplex.out'
    errout = out_dir + 'soplex.err'

# TEST CMDS
#soplex.cmd = [soplex.executable] + ['-m10000', soplex_run_dir + 'test.mps']
# REF CMDS
#soplex.cmd = [soplex.executable] + ['-m45000', 'pds-50.mps']
#soplex.cmd = [soplex.executable] + ['-m3500', soplex_run_dir + 'ref.mps']
#oplex.output = out_dir + 'soplex.out'
#oplex.errout = out_dir + 'soplex.err'

#453.povray
povray_run_dir = cpu2006_dir + \
        '453.povray/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Povray(Process):
    executable = povray_run_dir + 'povray' + alpha_suffix
    cmd = [executable] + ['SPEC-benchmark-test.ini']
    cwd = povray_run_dir
    output = out_dir + 'povray.out'
    errout = out_dir + 'povray.err'

# TEST CMDS
#povray.cmd = [povray.executable] + ['SPEC-benchmark-test.ini']
# REF CMDS
#povray.cmd = [povray.executable] + ['SPEC-benchmark-ref.ini']
#povray.output = out_dir + 'povray.out'
#povray.errout = out_dir + 'povray.err'

#454.calculix
calculix_run_dir = cpu2006_dir + \
        '454.calculix/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Calculix(Process):
    executable = calculix_run_dir + 'calculix' + alpha_suffix
    cmd = [executable] + ['-i', 'beampic']
    cwd = calculix_run_dir
    output = out_dir + 'calculix.out'
    errout = out_dir + 'calculix.err'

# TEST CMDS
#calculix.cmd = [calculix.executable] + ['-i', 'beampic']
# REF CMDS
#calculix.cmd = [calculix.executable] + ['-i', 'hyperviscoplastic']
#calculix.output = out_dir + 'calculix.out'
#calculix.errout = out_dir + 'calculix.err'

#456.hmmer
hmmer_run_dir = cpu2006_dir + \
        '456.hmmer/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Hmmer(Process):
    executable = hmmer_run_dir + 'hmmer' + alpha_suffix
    cmd = [executable] + ['--fixed', '0', '--mean', '325', '--num', '45000',
            '--sd', '200', '--seed', '0', hmmer_run_dir + 'bombesin.hmm']
    cwd = hmmer_run_dir
    output = out_dir + 'hmmer.out'
    errout = out_dir + 'hmmer.err'

#458.sjeng
sjeng_run_dir = cpu2006_dir + \
        '458.sjeng/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Sjeng(Process):
    executable = sjeng_run_dir + 'sjeng' + alpha_suffix
    cmd = [executable] + [sjeng_run_dir + 'test.txt']
    cwd = sjeng_run_dir
    output = out_dir + 'sjeng.out'
    errout = out_dir + 'sjeng.err'

# TEST CMDS
#sjeng.cmd = [sjeng.executable] + [sjeng_run_dir + 'test.txt']
# REF CMDS
#sjeng.cmd = [sjeng.executable] + [sjeng_run_dir + 'ref.txt']
#sjeng.output = out_dir + 'sjeng.out'
#sjeng.errout = out_dir + 'sjeng.err'

#459.GemsFDTD
GemsFDTD_run_dir = cpu2006_dir + \
        '459.GemsFDTD/run/run_base_test_i386-m32-gcc42-nn.0000/'
class GemsFDTD(Process):
    executable = GemsFDTD_run_dir + 'GemsFDTD' + alpha_suffix
    cmd = [executable]
    cwd = GemsFDTD_run_dir
    output = out_dir + 'GemsFDTD.out'
    errout = out_dir + 'GemsFDTD.err'

# TEST CMDS
#GemsFDTD.cmd = [GemsFDTD.executable]
# REF CMDS
#GemsFDTD.cmd = [GemsFDTD.executable]
#GemsFDTD.output = out_dir + 'GemsFDTD.out'
#GemsFDTD.errout = out_dir + 'GemsFDTD.err'

#462.libquantum
libquantum_run_dir = cpu2006_dir + \
        '462.libquantum/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Libquantum(Process):
    executable = libquantum_run_dir + 'libquantum' + alpha_suffix
    cmd = [executable] + ['33','5']
    cwd = libquantum_run_dir
    output = out_dir + 'libquantum.out'
    errout = out_dir + 'libquantum.err'

# TEST CMDS
#libquantum.cmd = [libquantum.executable] + ['33','5']
# REF CMDS
#libquantum.cmd = [libquantum.executable] + ['1297','8']
#libquantum.output = out_dir + 'libquantum.out'
#libquantum.errout = out_dir + 'libquantum.err'

#464.h264ref
h264ref_run_dir = cpu2006_dir + \
        '464.h264ref/run/run_base_test_i386-m32-gcc42-nn.0000/'
class H264ref(Process):
    executable = h264ref_run_dir + 'h264ref' + alpha_suffix
    cmd = [executable] + ['-d', h264ref_run_dir + \
            'foreman_test_encoder_baseline.cfg']
    cwd = h264ref_run_dir
    output = out_dir + 'h264ref.out'
    errout = out_dir + 'h264ref.err'

#465.tonto
tonto_run_dir = cpu2006_dir + \
        '465.tonto/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Tonto(Process):
    executable = tonto_run_dir + 'tonto' + alpha_suffix
    cmd = [executable]
    cwd = tonto_run_dir
    output = out_dir + 'tonto.out'
    errout = out_dir + 'tonto.err'


# TEST CMDS
#tonto.cmd = [tonto.executable]
# REF CMDS
#tonto.cmd = [tonto.executable]
#tonto.output = out_dir + 'tonto.out'
#tonto.errout = out_dir + 'tonto.err'

#470.lbm
lbm_run_dir = cpu2006_dir + \
        '470.lbm/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Lbm(Process):
    executable = lbm_run_dir + 'lbm' + alpha_suffix
    cmd = [executable] + ['20', lbm_run_dir + 'reference.dat',
            '0', '1', lbm_run_dir + '100_100_130_cf_a.of']
    cwd = lbm_run_dir
    output = out_dir + 'lbm.out'
    errout = out_dir + 'lbm.err'

#471.omnetpp
omnetpp_run_dir = cpu2006_dir + \
        '471.omnetpp/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Omnetpp(Process):
    executable = omnetpp_run_dir + 'omnetpp' + alpha_suffix
    cmd = [executable] + [omnetpp_run_dir + 'omnetpp.ini']
    cwd = omnetpp_run_dir
    output = out_dir + 'omnetpp.out'
    errout = out_dir + 'omnetpp.err'

# TEST CMDS
#omnetpp.cmd = [omnetpp.executable] + [omnetpp_run_dir + 'omnetpp.ini']
# REF CMDS
#omnetpp.cmd = [omnetpp.executable] + [omnetpp_run_dir + 'omnetpp.ini']
#omnetpp.output = out_dir + 'omnetpp.out'
#omnetpp.errout = out_dir + 'omnetpp.err'

#473.astar
astar_run_dir = cpu2006_dir + \
        '473.astar/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Astar(Process):
    executable = astar_run_dir + 'astar' + alpha_suffix
    cmd = [executable] + [astar_run_dir + 'lake.cfg']
    cwd = astar_run_dir
    output = out_dir + 'astar.out'
    errout = out_dir + 'astar.err'

# TEST CMDS
#astar.cmd = [astar.executable] + [astar_run_dir + 'lake.cfg']
# REF CMDS
#astar.cmd = [astar.executable] + [astar_run_dir + 'rivers.cfg']
#astar.output = out_dir + 'astar.out'
#astar.errout = out_dir + 'astar.err'

#481.wrf
wrf_run_dir = cpu2006_dir + \
        '481.wrf/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Wrf(Process):
    executable = wrf_run_dir + 'wrf' + alpha_suffix
    cmd = [executable]
    cwd = wrf_run_dir
    output = out_dir + 'wrf.out'
    errout = out_dir + 'wrf.err'

# TEST CMDS
#wrf.cmd = [wrf.executable]
# REF CMDS
#wrf.cmd = [wrf.executable]
#wrf.output = out_dir + 'wrf.out'
#wrf.errout = out_dir + 'wrf.err'

#482.sphinx3
sphinx3_run_dir = cpu2006_dir + \
        '482.sphinx3/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Sphinx3(Process):
    executable = sphinx3_run_dir + 'sphinx_livepretend' + alpha_suffix
    cmd = [executable] + ['ctlfile', '.', sphinx3_run_dir + 'args.an4']
    cwd = sphinx3_run_dir
    output = out_dir + 'sphinx3.out'
    errout = out_dir + 'sphinx3.err'

#483.xalancbmk
xalancbmk_run_dir = cpu2006_dir + \
        '483.xalancbmk/run/run_base_test_i386-m32-gcc42-nn.0000/'
xalancbmk=Process()
xalancbmk.executable = xalancbmk_run_dir + 'xalancbmk' + alpha_suffix
xalancbmk.output = out_dir + 'xalancbmk.out'
xalancbmk.errout = out_dir + 'xalancbmk.err'

#998.specrand
specrand_i_run_dir = cpu2006_dir + \
        '998.specrand/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Specrand_i(Process):
    executable = specrand_i_run_dir + 'specrand' + alpha_suffix
    cmd = [executable] + ['324342', '24239']
    cwd = specrand_i_run_dir
    output = out_dir + 'specrand_i.out'
    errout = out_dir + 'specrand_i.err'

# TEST CMDS
#specrand_i.cmd = [specrand_i.executable] + ['324342', '24239']
# REF CMDS
#specrand_i.cmd = [specrand_i.executable] + ['1255432124', '234923']
#specrand_i.output = out_dir + 'specrand_i.out'
#specrand_i.errout = out_dir + 'specrand_i.err'

#999.specrand
specrand_f_run_dir = cpu2006_dir + \
        '999.specrand/run/run_base_test_i386-m32-gcc42-nn.0000/'
class Specrand_f(Process):
    executable = specrand_f_run_dir + 'specrand' + alpha_suffix
    cmd = [executable] + ['324342', '24239']
    cwd = specrand_f_run_dir
    output = out_dir + 'specrand_f.out'
    errout = out_dir + 'specrand_f.err'

# TEST CMDS
#specrand_f.cmd = [specrand_f.executable] + ['324342', '24239']
# REF CMDS
#specrand_f.cmd = [specrand_f.executable] + ['1255432124', '234923']
#specrand_f.output = out_dir + 'specrand_f.out'
#specrand_f.errout = out_dir + 'specrand_f.err'
