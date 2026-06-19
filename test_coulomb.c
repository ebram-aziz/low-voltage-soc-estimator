
#include <stdio.h>
#include <math.h>
#include "soc_coulomb.h"

#define TOL 0.05f

static void assert_near(float expected, float actual)
{
    float diff = fabsf(expected - actual);

    if (diff < TOL)
        printf("[PASS]\n");
    else
        printf("[FAIL] expected %.3f got %.3f\n", expected, actual);
}

int main(void)
{
    Bms_SocState_t state = {0};

    SocCoulomb_Init(&state, 50.0f);

    /* 1Ah discharge on 60Ah battery */
    SocCoulomb_Update(&state, 60.0f, 60.0f);

    assert_near(48.333f, state.soc_pct);

    return 0;
}
