#ifndef CONFIG_H
#define CONFIG_H

/* 
 * a simple substitute for the config.h file normally provided by autoconf
 * from https://github.com/CloudI/CloudI/blob/master/src/m4/ax_clock_gettime.m4
 */
#include <unistd.h>
#include <time.h>
#if !defined(CLOCK_MONOTONIC) || !defined(_POSIX_MONOTONIC_CLOCK) || (_POSIX_MONOTONIC_CLOCK < 0)
#else
#define HAVE_CLOCK_GETTIME_MONOTONIC 1
#endif

#endif /* CONFIG_H */
