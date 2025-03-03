/* SPDX-FileCopyrightText: © 2022 Decompollaborate */
/* SPDX-License-Identifier: MIT */

/* Automatically generated. DO NOT MODIFY */

#ifndef Registers_enum_classes_table_h_automatic
#define Registers_enum_classes_table_h_automatic

    namespace Cpu {
        enum class GprO32 {
    GPR_O32_zero,
    GPR_O32_at,
    GPR_O32_v0,
    GPR_O32_v1,
    GPR_O32_a0,
    GPR_O32_a1,
    GPR_O32_a2,
    GPR_O32_a3,
    GPR_O32_t0,
    GPR_O32_t1,
    GPR_O32_t2,
    GPR_O32_t3,
    GPR_O32_t4,
    GPR_O32_t5,
    GPR_O32_t6,
    GPR_O32_t7,
    GPR_O32_s0,
    GPR_O32_s1,
    GPR_O32_s2,
    GPR_O32_s3,
    GPR_O32_s4,
    GPR_O32_s5,
    GPR_O32_s6,
    GPR_O32_s7,
    GPR_O32_t8,
    GPR_O32_t9,
    GPR_O32_k0,
    GPR_O32_k1,
    GPR_O32_gp,
    GPR_O32_sp,
    GPR_O32_fp,
    GPR_O32_ra,
        };
        enum class GprN32 {
    GPR_N32_zero,
    GPR_N32_at,
    GPR_N32_v0,
    GPR_N32_v1,
    GPR_N32_a0,
    GPR_N32_a1,
    GPR_N32_a2,
    GPR_N32_a3,
    GPR_N32_a4,
    GPR_N32_a5,
    GPR_N32_a6,
    GPR_N32_a7,
    GPR_N32_t0,
    GPR_N32_t1,
    GPR_N32_t2,
    GPR_N32_t3,
    GPR_N32_s0,
    GPR_N32_s1,
    GPR_N32_s2,
    GPR_N32_s3,
    GPR_N32_s4,
    GPR_N32_s5,
    GPR_N32_s6,
    GPR_N32_s7,
    GPR_N32_t8,
    GPR_N32_t9,
    GPR_N32_k0,
    GPR_N32_k1,
    GPR_N32_gp,
    GPR_N32_sp,
    GPR_N32_fp,
    GPR_N32_ra,
        };
        enum class Cop0 {
    COP0_Index,
    COP0_Random,
    COP0_EntryLo0,
    COP0_EntryLo1,
    COP0_Context,
    COP0_PageMask,
    COP0_Wired,
    COP0_Reserved07,
    COP0_BadVaddr,
    COP0_Count,
    COP0_EntryHi,
    COP0_Compare,
    COP0_Status,
    COP0_Cause,
    COP0_EPC,
    COP0_PRevID,
    COP0_Config,
    COP0_LLAddr,
    COP0_WatchLo,
    COP0_WatchHi,
    COP0_XContext,
    COP0_Reserved21,
    COP0_Reserved22,
    COP0_Reserved23,
    COP0_Reserved24,
    COP0_Reserved25,
    COP0_PErr,
    COP0_CacheErr,
    COP0_TagLo,
    COP0_TagHi,
    COP0_ErrorEPC,
    COP0_Reserved31,
        };
        enum class Cop1O32 {
    COP1_O32_fv0,
    COP1_O32_fv0f,
    COP1_O32_fv1,
    COP1_O32_fv1f,
    COP1_O32_ft0,
    COP1_O32_ft0f,
    COP1_O32_ft1,
    COP1_O32_ft1f,
    COP1_O32_ft2,
    COP1_O32_ft2f,
    COP1_O32_ft3,
    COP1_O32_ft3f,
    COP1_O32_fa0,
    COP1_O32_fa0f,
    COP1_O32_fa1,
    COP1_O32_fa1f,
    COP1_O32_ft4,
    COP1_O32_ft4f,
    COP1_O32_ft5,
    COP1_O32_ft5f,
    COP1_O32_fs0,
    COP1_O32_fs0f,
    COP1_O32_fs1,
    COP1_O32_fs1f,
    COP1_O32_fs2,
    COP1_O32_fs2f,
    COP1_O32_fs3,
    COP1_O32_fs3f,
    COP1_O32_fs4,
    COP1_O32_fs4f,
    COP1_O32_fs5,
    COP1_O32_fs5f,
        };
        enum class Cop1N32 {
    COP1_N32_fv0,
    COP1_N32_ft14,
    COP1_N32_fv1,
    COP1_N32_ft15,
    COP1_N32_ft0,
    COP1_N32_ft1,
    COP1_N32_ft2,
    COP1_N32_ft3,
    COP1_N32_ft4,
    COP1_N32_ft5,
    COP1_N32_ft6,
    COP1_N32_ft7,
    COP1_N32_fa0,
    COP1_N32_fa1,
    COP1_N32_fa2,
    COP1_N32_fa3,
    COP1_N32_fa4,
    COP1_N32_fa5,
    COP1_N32_fa6,
    COP1_N32_fa7,
    COP1_N32_fs0,
    COP1_N32_ft8,
    COP1_N32_fs1,
    COP1_N32_ft9,
    COP1_N32_fs2,
    COP1_N32_ft10,
    COP1_N32_fs3,
    COP1_N32_ft11,
    COP1_N32_fs4,
    COP1_N32_ft12,
    COP1_N32_fs5,
    COP1_N32_ft13,
        };
        enum class Cop1N64 {
    COP1_N64_fv0,
    COP1_N64_ft12,
    COP1_N64_fv1,
    COP1_N64_ft13,
    COP1_N64_ft0,
    COP1_N64_ft1,
    COP1_N64_ft2,
    COP1_N64_ft3,
    COP1_N64_ft4,
    COP1_N64_ft5,
    COP1_N64_ft6,
    COP1_N64_ft7,
    COP1_N64_fa0,
    COP1_N64_fa1,
    COP1_N64_fa2,
    COP1_N64_fa3,
    COP1_N64_fa4,
    COP1_N64_fa5,
    COP1_N64_fa6,
    COP1_N64_fa7,
    COP1_N64_ft8,
    COP1_N64_ft9,
    COP1_N64_ft10,
    COP1_N64_ft11,
    COP1_N64_fs0,
    COP1_N64_fs1,
    COP1_N64_fs2,
    COP1_N64_fs3,
    COP1_N64_fs4,
    COP1_N64_fs5,
    COP1_N64_fs6,
    COP1_N64_fs7,
        };
        enum class Cop1Control {
    COP1_CONTROL_0,
    COP1_CONTROL_1,
    COP1_CONTROL_2,
    COP1_CONTROL_3,
    COP1_CONTROL_4,
    COP1_CONTROL_5,
    COP1_CONTROL_6,
    COP1_CONTROL_7,
    COP1_CONTROL_8,
    COP1_CONTROL_9,
    COP1_CONTROL_10,
    COP1_CONTROL_11,
    COP1_CONTROL_12,
    COP1_CONTROL_13,
    COP1_CONTROL_14,
    COP1_CONTROL_15,
    COP1_CONTROL_16,
    COP1_CONTROL_17,
    COP1_CONTROL_18,
    COP1_CONTROL_19,
    COP1_CONTROL_20,
    COP1_CONTROL_21,
    COP1_CONTROL_22,
    COP1_CONTROL_23,
    COP1_CONTROL_24,
    COP1_CONTROL_25,
    COP1_CONTROL_26,
    COP1_CONTROL_27,
    COP1_CONTROL_28,
    COP1_CONTROL_29,
    COP1_CONTROL_30,
    COP1_CONTROL_FpcCsr,
        };
        enum class Cop2 {
    COP2_0,
    COP2_1,
    COP2_2,
    COP2_3,
    COP2_4,
    COP2_5,
    COP2_6,
    COP2_7,
    COP2_8,
    COP2_9,
    COP2_10,
    COP2_11,
    COP2_12,
    COP2_13,
    COP2_14,
    COP2_15,
    COP2_16,
    COP2_17,
    COP2_18,
    COP2_19,
    COP2_20,
    COP2_21,
    COP2_22,
    COP2_23,
    COP2_24,
    COP2_25,
    COP2_26,
    COP2_27,
    COP2_28,
    COP2_29,
    COP2_30,
    COP2_31,
        };
    };
    namespace Rsp {
        enum class Gpr {
    RSP_GPR_zero,
    RSP_GPR_1,
    RSP_GPR_2,
    RSP_GPR_3,
    RSP_GPR_4,
    RSP_GPR_5,
    RSP_GPR_6,
    RSP_GPR_7,
    RSP_GPR_8,
    RSP_GPR_9,
    RSP_GPR_10,
    RSP_GPR_11,
    RSP_GPR_12,
    RSP_GPR_13,
    RSP_GPR_14,
    RSP_GPR_15,
    RSP_GPR_16,
    RSP_GPR_17,
    RSP_GPR_18,
    RSP_GPR_19,
    RSP_GPR_20,
    RSP_GPR_21,
    RSP_GPR_22,
    RSP_GPR_23,
    RSP_GPR_24,
    RSP_GPR_25,
    RSP_GPR_26,
    RSP_GPR_27,
    RSP_GPR_28,
    RSP_GPR_29,
    RSP_GPR_30,
    RSP_GPR_ra,
        };
        enum class Cop0 {
    RSP_COP0_SP_MEM_ADDR,
    RSP_COP0_SP_DRAM_ADDR,
    RSP_COP0_SP_RD_LEN,
    RSP_COP0_SP_WR_LEN,
    RSP_COP0_SP_STATUS,
    RSP_COP0_SP_DMA_FULL,
    RSP_COP0_SP_DMA_BUSY,
    RSP_COP0_SP_SEMAPHORE,
    RSP_COP0_DPC_START,
    RSP_COP0_DPC_END,
    RSP_COP0_DPC_CURRENT,
    RSP_COP0_DPC_STATUS,
    RSP_COP0_DPC_CLOCK,
    RSP_COP0_DPC_BUFBUSY,
    RSP_COP0_DPC_PIPEBUSY,
    RSP_COP0_DPC_TMEM,
        };
        enum class Cop2 {
    RSP_COP2_0,
    RSP_COP2_1,
    RSP_COP2_2,
    RSP_COP2_3,
    RSP_COP2_4,
    RSP_COP2_5,
    RSP_COP2_6,
    RSP_COP2_7,
    RSP_COP2_8,
    RSP_COP2_9,
    RSP_COP2_10,
    RSP_COP2_11,
    RSP_COP2_12,
    RSP_COP2_13,
    RSP_COP2_14,
    RSP_COP2_15,
    RSP_COP2_16,
    RSP_COP2_17,
    RSP_COP2_18,
    RSP_COP2_19,
    RSP_COP2_20,
    RSP_COP2_21,
    RSP_COP2_22,
    RSP_COP2_23,
    RSP_COP2_24,
    RSP_COP2_25,
    RSP_COP2_26,
    RSP_COP2_27,
    RSP_COP2_28,
    RSP_COP2_29,
    RSP_COP2_30,
    RSP_COP2_31,
        };
        enum class Cop2Control {
    RSP_COP2_CONTROL_0,
    RSP_COP2_CONTROL_1,
    RSP_COP2_CONTROL_2,
    RSP_COP2_CONTROL_3,
    RSP_COP2_CONTROL_4,
    RSP_COP2_CONTROL_5,
    RSP_COP2_CONTROL_6,
    RSP_COP2_CONTROL_7,
    RSP_COP2_CONTROL_8,
    RSP_COP2_CONTROL_9,
    RSP_COP2_CONTROL_10,
    RSP_COP2_CONTROL_11,
    RSP_COP2_CONTROL_12,
    RSP_COP2_CONTROL_13,
    RSP_COP2_CONTROL_14,
    RSP_COP2_CONTROL_15,
    RSP_COP2_CONTROL_16,
    RSP_COP2_CONTROL_17,
    RSP_COP2_CONTROL_18,
    RSP_COP2_CONTROL_19,
    RSP_COP2_CONTROL_20,
    RSP_COP2_CONTROL_21,
    RSP_COP2_CONTROL_22,
    RSP_COP2_CONTROL_23,
    RSP_COP2_CONTROL_24,
    RSP_COP2_CONTROL_25,
    RSP_COP2_CONTROL_26,
    RSP_COP2_CONTROL_27,
    RSP_COP2_CONTROL_28,
    RSP_COP2_CONTROL_29,
    RSP_COP2_CONTROL_30,
    COP1_CONTROL_31,
        };
        enum class Vector {
    RSP_VECTOR_v0,
    RSP_VECTOR_v1,
    RSP_VECTOR_v2,
    RSP_VECTOR_v3,
    RSP_VECTOR_v4,
    RSP_VECTOR_v5,
    RSP_VECTOR_v6,
    RSP_VECTOR_v7,
    RSP_VECTOR_v8,
    RSP_VECTOR_v9,
    RSP_VECTOR_v10,
    RSP_VECTOR_v11,
    RSP_VECTOR_v12,
    RSP_VECTOR_v13,
    RSP_VECTOR_v14,
    RSP_VECTOR_v15,
    RSP_VECTOR_v16,
    RSP_VECTOR_v17,
    RSP_VECTOR_v18,
    RSP_VECTOR_v19,
    RSP_VECTOR_v20,
    RSP_VECTOR_v21,
    RSP_VECTOR_v22,
    RSP_VECTOR_v23,
    RSP_VECTOR_v24,
    RSP_VECTOR_v25,
    RSP_VECTOR_v26,
    RSP_VECTOR_v27,
    RSP_VECTOR_v28,
    RSP_VECTOR_v29,
    RSP_VECTOR_v30,
    RSP_VECTOR_v31,
        };
    };
    namespace R5900 {
        enum class VF {
R5900_VF_vf0,
R5900_VF_vf1,
R5900_VF_vf2,
R5900_VF_vf3,
R5900_VF_vf4,
R5900_VF_vf5,
R5900_VF_vf6,
R5900_VF_vf7,
R5900_VF_vf8,
R5900_VF_vf9,
R5900_VF_vf10,
R5900_VF_vf11,
R5900_VF_vf12,
R5900_VF_vf13,
R5900_VF_vf14,
R5900_VF_vf15,
R5900_VF_vf16,
R5900_VF_vf17,
R5900_VF_vf18,
R5900_VF_vf19,
R5900_VF_vf20,
R5900_VF_vf21,
R5900_VF_vf22,
R5900_VF_vf23,
R5900_VF_vf24,
R5900_VF_vf25,
R5900_VF_vf26,
R5900_VF_vf27,
R5900_VF_vf28,
R5900_VF_vf29,
R5900_VF_vf30,
R5900_VF_vf31,
        };
        enum class VI {
R5900_VI_vi0,
R5900_VI_vi1,
R5900_VI_vi2,
R5900_VI_vi3,
R5900_VI_vi4,
R5900_VI_vi5,
R5900_VI_vi6,
R5900_VI_vi7,
R5900_VI_vi8,
R5900_VI_vi9,
R5900_VI_vi10,
R5900_VI_vi11,
R5900_VI_vi12,
R5900_VI_vi13,
R5900_VI_vi14,
R5900_VI_vi15,
R5900_VI_vi16,
R5900_VI_vi17,
R5900_VI_vi18,
R5900_VI_vi19,
R5900_VI_vi20,
R5900_VI_vi21,
R5900_VI_vi22,
R5900_VI_vi23,
R5900_VI_vi24,
R5900_VI_vi25,
R5900_VI_vi26,
R5900_VI_vi27,
R5900_VI_vi28,
R5900_VI_vi29,
R5900_VI_vi30,
R5900_VI_vi31,
        };
    };

#endif
