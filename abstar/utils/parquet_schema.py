import pyarrow as pa

columns = [
    "seq_id",
    "chain",
    "v_gene",
    "d_gene",
    "j_gene",
    "assigner_scores",
    "vdj_assigner",
    "isotype",
    "isotype_score",
    "isotype_alignment",
    "nt_identity",
    "aa_identity",
    "junc_len",
    "cdr3_len",
    "vdj_nt",
    "gapped_vdj_nt",
    "cdr2_nt",
    "fr3_nt",
    "cdr3_nt",
    "fr4_nt",
    "vdj_germ_nt",
    "gapped_vdj_germ_nt",
    "junc_nt",
    "region_len_nt",
    "var_muts_nt",
    "join_muts_nt",
    "mut_count_nt",
    "vdj_aa",
    "fr3_aa",
    "cdr3_aa",
    "fr4_aa",
    "vdj_germ_aa",
    "junc_aa",
    "region_len_aa",
    "var_muts_aa",
    "join_muts_aa",
    "region_muts_nt",
    "region_muts_aa",
    "prod",
    "productivity_issues",
    "junction_in_frame",
    "raw_input",
    "oriented_input",
    "strand",
    "germ_alignments_nt",
    "exo_trimming",
    "junc_nt_breakdown",
    "germline_database",
    "species",
    "align_info",
    "j_del",
    "v_del",
    "j_ins",
    "v_ins",
]

dtypes = {
    "seq_id": str,
    "chain": str,
    "v_gene": str,
    "d_gene": str,
    "j_gene": str,
    "assigner_scores": str,
    "vdj_assigner": str,
    "isotype": str,
    "isotype_score": int,
    "isotype_alignment": str,
    "nt_identity": str,
    "aa_identity": str,
    "junc_len": int,
    "cdr3_len": int,
    "vdj_nt": str,
    "gapped_vdj_nt": str,
    "cdr2_nt": str,
    "fr3_nt": str,
    "cdr3_nt": str,
    "fr4_nt": str,
    "vdj_germ_nt": str,
    "gapped_vdj_germ_nt": str,
    "junc_nt": str,
    "region_len_nt": str,
    "var_muts_nt": str,
    "join_muts_nt": str,
    "mut_count_nt": int,
    "vdj_aa": str,
    "fr3_aa": str,
    "cdr3_aa": str,
    "fr4_aa": str,
    "vdj_germ_aa": str,
    "junc_aa": str,
    "region_len_aa": str,
    "var_muts_aa": str,
    "join_muts_aa": str,
    "region_muts_nt": str,
    "region_muts_aa": str,
    "prod": str,
    "productivity_issues": str,
    "junction_in_frame": str,
    "raw_input": str,
    "oriented_input": str,
    "strand": str,
    "germ_alignments_nt": str,
    "exo_trimming": str,
    "junc_nt_breakdown": str,
    "germline_database": str,
    "species": str,
    "align_info": str,
    "j_del": str,
    "v_del": str,
    "j_ins": str,
    "v_ins": str,
}


schema = pa.schema(
    [
        pa.field("seq_id", pa.string()),
        pa.field("chain", pa.string()),
        pa.field("vdj_assigner", pa.string()),
        pa.field("isotype", pa.string()),
        pa.field("isotype_score", pa.int64()),
        pa.field("junc_len", pa.int64()),
        pa.field("cdr3_len", pa.int64()),
        pa.field("vdj_nt", pa.string()),
        pa.field("vdj_aa", pa.string()),
        pa.field("gapped_vdj_nt", pa.string()),
        pa.field("vdj_germ_nt", pa.string()),
        pa.field("vdj_germ_aa", pa.string()),
        pa.field("gapped_vdj_germ_nt", pa.string()),
        pa.field("fr3_nt", pa.string()),
        pa.field("fr3_aa", pa.string()),
        pa.field("cdr3_nt", pa.string()),
        pa.field("cdr3_aa", pa.string()),
        pa.field("fr4_nt", pa.string()),
        pa.field("fr4_aa", pa.string()),
        pa.field("junc_nt", pa.string()),
        pa.field("junc_aa", pa.string()),
        pa.field("cdr2_nt", pa.string()),
        pa.field("mut_count_nt", pa.int64()),
        pa.field("prod", pa.string()),
        pa.field("productivity_issues", pa.string()),
        pa.field("junction_in_frame", pa.string()),
        pa.field("raw_input", pa.string()),
        pa.field("oriented_input", pa.string()),
        pa.field("strand", pa.string()),
        pa.field("germline_database", pa.string()),
        pa.field("species", pa.string()),
        pa.field(
            "v_gene",
            pa.struct(
                [
                    pa.field("full", pa.string()),
                    pa.field("fam", pa.string()),
                    pa.field("gene", pa.string()),
                    pa.field("score", pa.int64()),
                    pa.field("assigner_score", pa.float64()),
                    pa.field(
                        "others",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("full", pa.string()),
                                    pa.field("assigner_score", pa.float64()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "d_gene",
            pa.struct(
                [
                    pa.field("full", pa.string()),
                    pa.field("fam", pa.string()),
                    pa.field("gene", pa.string()),
                    pa.field("score", pa.int64()),
                    pa.field("assigner_score", pa.int64()),
                    pa.field(
                        "others",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("full", pa.string()),
                                    pa.field("assigner_score", pa.int64()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "j_gene",
            pa.struct(
                [
                    pa.field("full", pa.string()),
                    pa.field("gene", pa.string()),
                    pa.field("score", pa.int64()),
                    pa.field("assigner_score", pa.float64()),
                    pa.field(
                        "others",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("full", pa.string()),
                                    pa.field("assigner_score", pa.float64()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "assigner_scores",
            pa.struct(
                [
                    pa.field("v", pa.float64()),
                    pa.field("d", pa.int64()),
                    pa.field("j", pa.float64()),
                ]
            ),
        ),
        pa.field(
            "isotype_alignment",
            pa.struct(
                [
                    pa.field("query", pa.string()),
                    pa.field("midline", pa.string()),
                    pa.field("isotype", pa.string()),
                ]
            ),
        ),
        pa.field(
            "nt_identity",
            pa.struct(
                [
                    pa.field("v", pa.float64()),
                    pa.field("j", pa.float64()),
                ]
            ),
        ),
        pa.field(
            "aa_identity",
            pa.struct(
                [
                    pa.field("v", pa.float64()),
                    pa.field("j", pa.float64()),
                ]
            ),
        ),
        pa.field(
            "region_len_nt",
            pa.struct(
                [
                    pa.field("fr1", pa.int64()),
                    pa.field("cdr1", pa.int64()),
                    pa.field("fr2", pa.int64()),
                    pa.field("cdr2", pa.int64()),
                    pa.field("fr3", pa.int64()),
                    pa.field("cdr3", pa.int64()),
                    pa.field("fr4", pa.int64()),
                ]
            ),
        ),
        pa.field(
            "region_len_aa",
            pa.struct(
                [
                    pa.field("fr1", pa.int64()),
                    pa.field("cdr1", pa.int64()),
                    pa.field("fr2", pa.int64()),
                    pa.field("cdr2", pa.int64()),
                    pa.field("fr3", pa.int64()),
                    pa.field("cdr3", pa.int64()),
                    pa.field("fr4", pa.int64()),
                ]
            ),
        ),
        pa.field(
            "var_muts_nt",
            pa.struct(
                [
                    pa.field("num", pa.int64()),
                    pa.field(
                        "muts",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("was", pa.string()),
                                    pa.field("is", pa.string()),
                                    pa.field("raw_position", pa.string()),
                                    pa.field("position", pa.string()),
                                    pa.field("codon", pa.string()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "var_muts_aa",
            pa.struct(
                [
                    pa.field("num", pa.int64()),
                    pa.field(
                        "muts",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("was", pa.string()),
                                    pa.field("is", pa.string()),
                                    pa.field("raw_position", pa.string()),
                                    pa.field("position", pa.string()),
                                    pa.field("codon", pa.string()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "join_muts_nt",
            pa.struct(
                [
                    pa.field("num", pa.int64()),
                    pa.field(
                        "muts",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("was", pa.string()),
                                    pa.field("is", pa.string()),
                                    pa.field("raw_position", pa.string()),
                                    pa.field("position", pa.string()),
                                    pa.field("codon", pa.string()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "join_muts_aa",
            pa.struct(
                [
                    pa.field("num", pa.int64()),
                    pa.field(
                        "muts",
                        pa.list_(
                            pa.struct(
                                [
                                    pa.field("was", pa.string()),
                                    pa.field("is", pa.string()),
                                    pa.field("raw_position", pa.string()),
                                    pa.field("position", pa.string()),
                                    pa.field("codon", pa.string()),
                                ]
                            )
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "region_muts_nt",
            pa.struct(
                [
                    pa.field(
                        "fr1",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr1",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr2",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr2",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr3",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr3",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr4",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "region_muts_aa",
            pa.struct(
                [
                    pa.field(
                        "fr1",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr1",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr2",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr2",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr3",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "cdr3",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    pa.field(
                        "fr4",
                        pa.struct(
                            [
                                pa.field("num", pa.int64()),
                                pa.field(
                                    "muts",
                                    pa.list_(
                                        pa.struct(
                                            [
                                                pa.field("was", pa.string()),
                                                pa.field("is", pa.string()),
                                                pa.field("raw_position", pa.string()),
                                                pa.field("position", pa.string()),
                                                pa.field("codon", pa.string()),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "germ_alignments_nt",
            pa.struct(
                [
                    pa.field(
                        "var",
                        pa.struct(
                            [
                                pa.field("query", pa.string()),
                                pa.field("germ", pa.string()),
                                pa.field("midline", pa.string()),
                            ]
                        ),
                    ),
                    pa.field(
                        "join",
                        pa.struct(
                            [
                                pa.field("query", pa.string()),
                                pa.field("germ", pa.string()),
                                pa.field("midline", pa.string()),
                            ]
                        ),
                    ),
                    pa.field(
                        "div",
                        pa.struct(
                            [
                                pa.field("query", pa.string()),
                                pa.field("germ", pa.string()),
                                pa.field("midline", pa.string()),
                            ]
                        ),
                    ),
                ]
            ),
        ),
        pa.field(
            "exo_trimming",
            pa.struct(
                [
                    pa.field("var_3", pa.int64()),
                    pa.field("join_5", pa.int64()),
                    pa.field("div_5", pa.int64()),
                    pa.field("div_3", pa.int64()),
                ]
            ),
        ),
        pa.field(
            "junc_nt_breakdown",
            pa.struct(
                [
                    pa.field("v_nt", pa.string()),
                    pa.field("n_nt", pa.string()),
                    pa.field("n1_nt", pa.string()),
                    pa.field("d_nt", pa.string()),
                    pa.field("n2_nt", pa.string()),
                    pa.field("j_nt", pa.string()),
                    pa.field("d_dist_from_cdr3_start", pa.int64()),
                    pa.field("d_dist_from_cdr3_end", pa.int64()),
                ]
            ),
        ),
        pa.field(
            "align_info",
            pa.struct(
                [
                    pa.field("v_start", pa.int64()),
                    pa.field("v_end", pa.int64()),
                    pa.field("d_start", pa.int64()),
                    pa.field("d_end", pa.int64()),
                    pa.field("j_start", pa.int64()),
                    pa.field("j_end", pa.int64()),
                ]
            ),
        ),
        pa.field(
            "j_del",
            pa.list_(
                pa.struct(
                    [
                        pa.field("in_frame", pa.string()),
                        pa.field("length", pa.int64()),
                        pa.field("sequence", pa.string()),
                        pa.field("position", pa.string()),
                        pa.field("codon", pa.string()),
                    ]
                )
            ),
        ),
        pa.field(
            "v_del",
            pa.list_(
                pa.struct(
                    [
                        pa.field("in_frame", pa.string()),
                        pa.field("length", pa.int64()),
                        pa.field("sequence", pa.string()),
                        pa.field("position", pa.string()),
                        pa.field("codon", pa.string()),
                    ]
                )
            ),
        ),
        pa.field(
            "j_ins",
            pa.list_(
                pa.struct(
                    [
                        pa.field("in_frame", pa.string()),
                        pa.field("length", pa.int64()),
                        pa.field("sequence", pa.string()),
                        pa.field("position", pa.string()),
                        pa.field("codon", pa.string()),
                    ]
                )
            ),
        ),
        pa.field(
            "v_ins",
            pa.list_(
                pa.struct(
                    [
                        pa.field("in_frame", pa.string()),
                        pa.field("length", pa.int64()),
                        pa.field("sequence", pa.string()),
                        pa.field("position", pa.string()),
                        pa.field("codon", pa.string()),
                    ]
                )
            ),
        ),
    ]
)
