`timescale 1ns / 1ns
module ofb_enc_test();
 reg clk;  
 reg [1:64] key;
 reg [1:64] nonce;
 reg [1:8388606] full_input[1:1]; 
                             
 reg [1:8388608] input_grayscale_values;
 wire [1:8388608] final;
 
ofb_enc a(final,input_grayscale_values,key,nonce,clk); 
initial
begin
/*
    ******
    ******
    CHANGE FILE LOCATION IN THE VARIABLE BELOW AS PER YOUR PC
    ******
    ******
    */ 
$readmemb("D:/I-CHIP_2bits/input.txt", full_input); 
 
input_grayscale_values=full_input[1];

clk=1'b0;
key=64'b11011010_11011010_11011010_11011010_11011010_11011010_11011010_11011010;
nonce=64'b11010010_11011010_11011010_11011010_11000010_11011010_11011010_11011010;
forever 
begin
#5 clk=~clk; 
end
end

endmodule