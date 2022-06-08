/* SPDX-FileCopyrightText: © 2022 Decompollaborate */
/* SPDX-License-Identifier: MIT */

#include "instructions/RabbitizerInstrDescriptor.h"

#include "instructions/RabbitizerInstruction.h"


#define RABBITIZER_DEF_INSTR_ID(prefix, name, ...) \
    [RABBITIZER_INSTR_ID_##prefix##_##name] = { __VA_ARGS__ }

#define RABBITIZER_DEF_INSTR_ID_ALTNAME(prefix, name, altname, ...) \
    [RABBITIZER_INSTR_ID_##prefix##_##name] = { __VA_ARGS__ }


const RabbitizerInstrDescriptor RabbitizerInstrDescriptor_Descriptors[] = {
    #include "instructions/instr_id/RabbitizerInstrId_cpu.inc"
    #include "instructions/instr_id/RabbitizerInstrId_rsp.inc"
};

#undef RABBITIZER_DEF_INSTR_ID
#undef RABBITIZER_DEF_INSTR_ID_ALTNAME


bool RabbitizerInstrDescriptor_isJType(const RabbitizerInstrDescriptor *self) {
    return self->instrType == RABBITIZER_INSTR_TYPE_J;
}
bool RabbitizerInstrDescriptor_isIType(const RabbitizerInstrDescriptor *self) {
    return self->instrType == RABBITIZER_INSTR_TYPE_I;
}
bool RabbitizerInstrDescriptor_isRType(const RabbitizerInstrDescriptor *self) {
    return self->instrType == RABBITIZER_INSTR_TYPE_R;
}

bool RabbitizerInstrDescriptor_isBranch(const RabbitizerInstrDescriptor *self) {
    return self->isBranch;
}
bool RabbitizerInstrDescriptor_isBranchLikely(const RabbitizerInstrDescriptor *self) {
    return self->isBranchLikely;
}
bool RabbitizerInstrDescriptor_isJump(const RabbitizerInstrDescriptor *self) {
    return self->isJump;
}
bool RabbitizerInstrDescriptor_isTrap(const RabbitizerInstrDescriptor *self) {
    return self->isTrap;
}

bool RabbitizerInstrDescriptor_isFloat(const RabbitizerInstrDescriptor *self) {
    return self->isFloat;
}
bool RabbitizerInstrDescriptor_isDouble(const RabbitizerInstrDescriptor *self) {
    return self->isDouble;
}

bool RabbitizerInstrDescriptor_isUnsigned(const RabbitizerInstrDescriptor *self) {
    return self->isUnsigned;
}

bool RabbitizerInstrDescriptor_modifiesRt(const RabbitizerInstrDescriptor *self) {
    return self->modifiesRt;
}
bool RabbitizerInstrDescriptor_modifiesRd(const RabbitizerInstrDescriptor *self) {
    return self->modifiesRd;
}
