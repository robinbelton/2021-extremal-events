READ ME 3/8/22
Sophia Campione

Data:
Note: Lifeline data was causing issues when running DlxJTK because the timepoints aren't evenly distributed.
Ran the original Tina data instead (which is identical to the lifeline data, but with different TP labeling).
Data can be found in the DLxJTK folder in input_files: crypto_rnaseq_norm_trim.tsv

Process:
1. Trimmed timepoint 0 to remove potential stress response.
2. Ran DLxJTK using periods 60, 70, 80. --> Results in node_finding_20220308090355.
3. Filtered DLxJTK results using IDV_filter_sort_file with annotations from Rob and from previous Haase Lab Papers. --> Subsetted DLxJTK results to only include TFs from Jung 2015, clbs/clns & wavepool from Rob's filtering file, and APC.
Added annotation column containing whether the gene is a TF, Cyclin/Kinase, or Ubiquitin Ligase. Added another column containing the source of the annotation.
See Jupyter Notebook crytpo_dlxjtk_annot.ipynb for details/process.
Filtered file is dlxjtk_filtered.tsv in node_finding_20220308090355.
