montage -geometry +1+1 n5_sample_GSR_raw.png  n5_sample_GSR_normalized.png n5_t1_GSR_raw.png n5_t1_GSR_normalized.png n5_t2_GSR_raw.png n5_t2_GSR_normalized.png n5_t3_GSR_raw.png n5_t3_GSR_normalized.png out.png
convert out.png plots_GSR_n5.pdf
rm out.pngmontage -geometry +1+1 n5_sample_TEMP_raw.png  n5_sample_TEMP_normalized.png n5_t1_TEMP_raw.png n5_t1_TEMP_normalized.png n5_t2_TEMP_raw.png n5_t2_TEMP_normalized.png n5_t3_TEMP_raw.png n5_t3_TEMP_normalized.png out.png
convert out.png plots_TEMP_n5.pdf
rm out.png