import numpy as np

def factor(bb):
    """
    Factor out site-based delay and rate from baseline-based slopes

    The linear drift (slopes) of phase with frequency and time are
    usually interpreted as delays and rates, and are removed from the
    VLBI data in fringe fitting.  Let n be the number of sites.  There
    are n (n-1) such slopes in total.  Using all of them, such as
    currently done in HOPS, breaks the closure relationships in
    general.

    Global fringe solution takes into account the assumption that
    delays and rates are site-based.  The main advantage is that it
    preserves the closure relationships.  Even better, "one person's
    noise is another person's signal", the remaining slopes after
    global fringe fit actually contain information about the source
    images.  Being able to factor out these site-based "noise" from
    the baseline-based "data", therefore, is essential for developing
    new high-order image reconstruction methods.

    We implement here a very general approach to factor out site-based
    information from baseline-based information.  Let obs[] be the
    observational data and sol[] be the solution array, the simplest
    error function is

        err[ref, rem] = obs[ref, rem] - (sol[ref] - sol[rem])

    However, it is clear that sol[] is not uniquely determined because
    err[ref, rem] is invariant to a global constant offset to sol[].

    Args:
        bb:    Baseline-based input data

    Returns:
        Site-based data being factored out

    """
    sites = np.unique(np.append(bb['ref'], bb['rem']))
    types = [('site', sites.dtype), ('value', 'f8')]
    sb    = np.array([(s, 0) for s in sites], dtype=types)

    return sb
