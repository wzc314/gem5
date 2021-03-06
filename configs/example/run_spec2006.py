# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Steve Reinhardt

# Simple test script
#
# "m5 test.py"

import optparse
import sys
import os

import spec2006_benchmarks
from spec2006_benchmarks import Bzip2, Gcc, Soplex, Mcf, Milc, GemsFDTD, \
        Libquantum, Omnetpp, Tonto, Perlbench, Wrf, Namd

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.util import addToPath, fatal

addToPath('../')

from ruby import Ruby

from common import Options
from common import Simulation
from common import CacheConfig
from common import CpuConfig
from common import MemConfig
from common.Caches import *
from common.cpu2000 import *

# Check if KVM support has been enabled, we might need to do VM
# configuration if that's the case.
have_kvm_support = 'BaseKvmCPU' in globals()
def is_kvm_cpu(cpu_class):
    return have_kvm_support and cpu_class != None and \
        issubclass(cpu_class, BaseKvmCPU)

m5.disableAllListeners()
parser = optparse.OptionParser()
Options.addCommonOptions(parser)
Options.addSEOptions(parser)

#在后面加入下面几行选项
parser.add_option("-b", "--benchmarks", type="string", default="",
        help="The SPEC benchmark to be loaded.")
parser.add_option("--benchmark_stdout", type="string", default="",
        help="Absolute path for stdout redirection for the benchmark.")
parser.add_option("--benchmark_stderr", type="string", default="",
        help="Absolute path for stderr redirection for the benchmark.")

if '--ruby' in sys.argv:
    Ruby.define_options(parser)

(options, args) = parser.parse_args()

if args:
    print "Error: script doesn't take any positional arguments"
    sys.exit(1)

numThreads = 1

def get_process(benchmark, idx):
    if benchmark == 'perlbench':
        process = spec2006_benchmarks.Perlbench()
    elif benchmark == 'bzip2':
        process = spec2006_benchmarks.Bzip2()
    elif benchmark == 'gcc':
        process = spec2006_benchmarks.Gcc()
    elif benchmark == 'bwaves':
        process = spec2006_benchmarks.Bwaves()
    elif benchmark == 'gamess':
        process = spec2006_benchmarks.Gamess()
    elif benchmark == 'mcf':
        process = spec2006_benchmarks.Mcf()
    elif benchmark == 'milc':
        process = spec2006_benchmarks.Milc()
    elif benchmark == 'zeusmp':
        process = spec2006_benchmarks.Zeusmp()
    elif benchmark == 'gromacs':
        process = spec2006_benchmarks.Gromacs()
    elif benchmark == 'cactusADM':
        process = spec2006_benchmarks.CactusADM()
    elif benchmark == 'leslie3d':
        process = spec2006_benchmarks.Leslie3d()
    elif benchmark == 'namd':
        process = spec2006_benchmarks.Namd()
    elif benchmark == 'gobmk':
        process = spec2006_benchmarks.Gobmk()
    elif benchmark == 'dealII':
        process = spec2006_benchmarks.DealII()
    elif benchmark == 'soplex':
        process = spec2006_benchmarks.Soplex()
    elif benchmark == 'povray':
        process = spec2006_benchmarks.Povray()
    elif benchmark == 'calculix':
        process = spec2006_benchmarks.Calculix()
    elif benchmark == 'hmmer':
        process = spec2006_benchmarks.Hmmer()
    elif benchmark == 'sjeng':
        process = spec2006_benchmarks.Sjeng()
    elif benchmark == 'GemsFDTD':
        process = spec2006_benchmarks.GemsFDTD()
    elif benchmark == 'libquantum':
        process = spec2006_benchmarks.Libquantum()
    elif benchmark == 'h264ref':
        process = spec2006_benchmarks.H264ref()
    elif benchmark == 'tonto':
        process = spec2006_benchmarks.Tonto()
    elif benchmark == 'lbm':
        process = spec2006_benchmarks.Lbm()
    elif benchmark == 'omnetpp':
        process = spec2006_benchmarks.Omnetpp()
    elif benchmark == 'astar':
        process = spec2006_benchmarks.Astar()
    elif benchmark == 'wrf':
        process = spec2006_benchmarks.Wrf()
    elif benchmark == 'sphinx3':
        process = spec2006_benchmarks.Sphinx3()
    elif benchmark == 'xalancbmk':
        process = spec2006_benchmarks.Xalancbmk()
    elif benchmark == 'specrand_i':
        process = spec2006_benchmarks.Specrand_i()
    elif benchmark == 'specrand_f':
        process = spec2006_benchmarks.Specrand_f()
    else:
        print >> sys.stderr, "Need --benchmarks switch to specify SPEC \
                CPU2006 workload. Exiting!\n"
        sys.exit(1)
    process.pid = 100 + idx
    return process

benchmarks = options.benchmarks.split(',')
if len(benchmarks) != options.num_cpus:
    print "Number of benchmarks not equal to set num_cpus!"
    sys.exit(1)

multiprocesses = []
idx = 0
for benchmark in benchmarks:
    process = get_process(benchmark, idx)
    multiprocesses.append(process)
    idx += 1


(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(options)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if options.smt and options.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = options.num_cpus
system = System(cpu = [CPUClass(cpu_id=i) for i in xrange(np)],
                mem_mode = test_mem_mode,
                mem_ranges = [AddrRange(options.mem_size)],
                cache_line_size = options.cacheline_size)

if numThreads > 1:
    system.multi_thread = True

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage = options.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(clock =  options.sys_clock,
                                   voltage_domain = system.voltage_domain)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(clock = options.cpu_clock,
                                       voltage_domain =
                                       system.cpu_voltage_domain)

# If elastic tracing is enabled, then configure the cpu and attach the elastic
# trace probe
if options.elastic_trace_en:
    CpuConfig.config_etrace(CPUClass, system.cpu, options)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

if is_kvm_cpu(CPUClass) or is_kvm_cpu(FutureClass):
    if buildEnv['TARGET_ISA'] == 'x86':
        system.vm = KvmVM()
        for process in multiprocesses:
            process.useArchPT = True
            process.kvmInSE = True
    else:
        fatal("KvmCPU can only be used in SE mode with x86")

# Sanity check
if options.fastmem:
    if CPUClass != AtomicSimpleCPU:
        fatal("Fastmem can only be used with atomic CPU!")
    if (options.caches or options.l2cache):
        fatal("You cannot use fastmem in combination with caches!")

if options.simpoint_profile:
    if not options.fastmem:
        # Atomic CPU checked with fastmem option already
        fatal("SimPoint generation should be done with atomic cpu and fastmem")
    if np > 1:
        fatal("SimPoint generation not supported with more than one CPUs")

for i in xrange(np):
    system.cpu[i].workload = multiprocesses[i]
    print 'cpu[%d] workload cmd --> %s' % (i, multiprocesses[i].cmd)
    system.cpu[i].createThreads()

if options.ruby:
    if options.cpu_type == "atomic" or options.cpu_type == "AtomicSimpleCPU":
        print >> sys.stderr, "Ruby does not work with atomic cpu!!"
        sys.exit(1)

    Ruby.create_system(options, False, system)
    assert(options.num_cpus == len(system.ruby._cpu_ports))

    system.ruby.clk_domain = SrcClockDomain(clock = options.ruby_clock,
                                        voltage_domain = system.voltage_domain)
    for i in xrange(np):
        ruby_port = system.ruby._cpu_ports[i]

        # Create the interrupt controller and connect its ports to Ruby
        # Note that the interrupt controller is always present but only
        # in x86 does it have message ports that need to be connected
        system.cpu[i].createInterruptController()

        # Connect the cpu's cache ports to Ruby
        system.cpu[i].icache_port = ruby_port.slave
        system.cpu[i].dcache_port = ruby_port.slave
        if buildEnv['TARGET_ISA'] == 'x86':
            system.cpu[i].interrupts[0].pio = ruby_port.master
            system.cpu[i].interrupts[0].int_master = ruby_port.slave
            system.cpu[i].interrupts[0].int_slave = ruby_port.master
            system.cpu[i].itb.walker.port = ruby_port.slave
            system.cpu[i].dtb.walker.port = ruby_port.slave
else:
    MemClass = Simulation.setMemClass(options)
    system.membus = SystemXBar()
    system.system_port = system.membus.slave
    CacheConfig.config_cache(options, system)
    MemConfig.config_mem(options, system)

root = Root(full_system = False, system = system)
Simulation.run(options, root, system, FutureClass)
