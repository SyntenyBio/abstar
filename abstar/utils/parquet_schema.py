import pyarrow as pa

schema = {
    "v_gene": pa.struct(
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
    "d_gene": pa.struct(
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
    "j_gene": pa.struct(
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
    "assigner_scores": pa.struct(
        [
            pa.field("v", pa.float64()),
            pa.field("d", pa.int64()),
            pa.field("j", pa.float64()),
        ]
    ),
    "isotype_alignment": pa.struct(
        [
            pa.field("query", pa.string()),
            pa.field("midline", pa.string()),
            pa.field("isotype", pa.string()),
        ]
    ),
    "nt_identity": pa.struct(
        [
            pa.field("v", pa.float64()),
            pa.field("j", pa.float64()),
        ]
    ),
    "aa_identity": pa.struct(
        [
            pa.field("v", pa.float64()),
            pa.field("j", pa.float64()),
        ]
    ),
    "region_len_nt": pa.struct(
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
    "region_len_aa": pa.struct(
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
    "var_muts_nt": pa.struct(
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
    "var_muts_aa": pa.struct(
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
    "join_muts_nt": pa.struct(
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
    "join_muts_aa": pa.struct(
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
    "region_muts_nt": pa.struct(
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
    "region_muts_aa": pa.struct(
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
    "germ_alignments_nt": pa.struct(
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
    "exo_trimming": pa.struct(
        [
            pa.field("var_3", pa.int64()),
            pa.field("join_5", pa.int64()),
            pa.field("div_5", pa.int64()),
            pa.field("div_3", pa.int64()),
        ]
    ),
    "junc_nt_breakdown": pa.struct(
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
    "align_info": pa.struct(
        [
            pa.field("v_start", pa.int64()),
            pa.field("v_end", pa.int64()),
            pa.field("d_start", pa.int64()),
            pa.field("d_end", pa.int64()),
            pa.field("j_start", pa.int64()),
            pa.field("j_end", pa.int64()),
        ]
    ),
}
