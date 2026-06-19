
#include "soc_coulomb.h"

void SocCoulomb_Init(Bms_SocState_t *state, float initial_soc_pct)
{
    if (!state) return;

    state->soc_pct = initial_soc_pct;
    state->soc_prev_pct = initial_soc_pct;
    state->is_initialised = true;
}

/* Positive current = discharge
 * Negative current = charge
 */
Bms_Error_t SocCoulomb_Update(Bms_SocState_t *state,
                              float current_a,
                              float dt_s)
{
    if (!state || !state->is_initialised)
    {
        return BMS_ERR_NOT_INITIALISED;
    }

    float eta = (current_a >= 0.0f)
                ? BMS_COULOMBIC_EFF_DCHG
                : BMS_COULOMBIC_EFF_CHG;

    float delta_soc =
        (current_a * dt_s * eta) /
        (3600.0f * BMS_CELL_CAPACITY_AH) * 100.0f;

    state->soc_prev_pct = state->soc_pct;

    /* Discharge reduces SOC */
    state->soc_pct -= delta_soc;

    if (state->soc_pct > 100.0f) state->soc_pct = 100.0f;
    if (state->soc_pct < 0.0f)   state->soc_pct = 0.0f;

    return BMS_OK;
}
