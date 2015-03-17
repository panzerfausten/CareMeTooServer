montage -geometry +1+1 n3_sample_GSR_raw.png  n3_sample_GSR_normalized.png n3_t1_GSR_raw.png n3_t1_GSR_normalized.png n3_t2_GSR_raw.png n3_t2_GSR_normalized.png n3_t3_GSR_raw.png n3_t3_GSR_normalized.png out.png
convert out.png plots_GSR_n3.pdf
rm out.pngmontage -geometry +1+1 n3_sample_TEMP_raw.png  n3_sample_TEMP_normalized.png n3_t1_TEMP_raw.png n3_t1_TEMP_normalized.png n3_t2_TEMP_raw.png n3_t2_TEMP_normalized.png n3_t3_TEMP_raw.png n3_t3_TEMP_normalized.png out.png
convert out.png plots_TEMP_n3.pdf
rm out.png