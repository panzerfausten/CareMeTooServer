montage -geometry +1+1 n8_sample_GSR_raw.png  n8_sample_GSR_normalized.png n8_t1_GSR_raw.png n8_t1_GSR_normalized.png n8_t2_GSR_raw.png n8_t2_GSR_normalized.png n8_t3_GSR_raw.png n8_t3_GSR_normalized.png out.png
convert out.png plots_GSR_n8.pdf
rm out.pngmontage -geometry +1+1 n8_sample_TEMP_raw.png  n8_sample_TEMP_normalized.png n8_t1_TEMP_raw.png n8_t1_TEMP_normalized.png n8_t2_TEMP_raw.png n8_t2_TEMP_normalized.png n8_t3_TEMP_raw.png n8_t3_TEMP_normalized.png out.png
convert out.png plots_TEMP_n8.pdf
rm out.png