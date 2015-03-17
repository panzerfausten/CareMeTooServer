montage -geometry +1+1 n2_sample_GSR_raw.png  n2_sample_GSR_normalized.png n2_t1_GSR_raw.png n2_t1_GSR_normalized.png n2_t2_GSR_raw.png n2_t2_GSR_normalized.png n2_t3_GSR_raw.png n2_t3_GSR_normalized.png out.png
convert out.png plots_GSR_n2.pdf
rm out.png
montage -geometry +1+1 n2_sample_TEMP_raw.png  n2_sample_TEMP_normalized.png n2_t1_TEMP_raw.png n2_t1_TEMP_normalized.png n2_t2_TEMP_raw.png n2_t2_TEMP_normalized.png n2_t3_TEMP_raw.png n2_t3_TEMP_normalized.png out.png
convert out.png plots_TEMP_n2.pdf
rm out.png
