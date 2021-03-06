`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
//
// Create Date:    10:57:50 04/23/2017
// Design Name: 	 umd-ctf 2017
// Module Name:    encrypt
//
//////////////////////////////////////////////////////////////////////////////////
module encrypt(
  input clk,
  input reset,
  input wire [127:0] m,
  output reg [127:0] n,
  output reg [127:0] d,
  output reg [127:0] c
);

reg [5:0] count;
reg [4:0] e;

always @ (posedge clk or reset)
begin
  if (reset)
  begin
    count <= 5'b0;
    n <= 128'b0;
    d <= 128'b0;
    c <= 128'b0;
    e <= 128'b10001;
  end
  else
  begin
    case(count)
      6'b000000:
      begin
        n[127:124] <= 1 + 2 + 3;
        d[127:124] <= -2 + (4 << 1);
      end

      6'b000001:
      begin
        n[19:16] <= n[127:124] + 3;
        d[71:68] <= 12 ^ d[127:124];
      end

      6'b000010:
      begin
        n[111:108] <= n[19:16] - 2;
        d[111:108] <= d[71:68] | 5;
      end

      6'b000011:
      begin
        n[107:104] <= n[111:108] - 1;
        d[43:40] <= d[111:108] & 0;
      end

      6'b000100:
      begin
        n[11:8] <= n[107:104] | 15;
        d[27:24] <= d[43:40] + (1 << 1);
      end

      6'b000101:
      begin
        n[27:24] <= n[11:8] - 3;
        d[3:0] <= d[27:24] >> 1;
      end

      6'b000110:
      begin
        n[47:44] <= n[27:24] | 1;
        d[91:88] <= (d[3:0] << 3) + (d[3:0] << 1);
      end

      6'b000111:
      begin
        n[83:80] <= n[47:44] & 5;
        d[99:96] <= 2 + (d[91:88] >> 1);
      end

      6'b001000:
      begin
        n[3:0] <= 2 + (n[83:80] >> 2);
        d[83:80] <= 8 + (d[99:96] ^ 6);
      end

      6'b001001:
      begin
        n[43:40] <= n[3:0] << 2;
        d[15:12] <= d[83:80] - 9;
      end

      6'b001010:
      begin
        n[91:88] <= n[43:40] | 2;
        d[79:76] <= d[15:12] & 0;
      end

      6'b001011:
      begin
        n[35:32] <= n[91:88] - 6;
        d[67:64] <= d[79:76] | 1;
      end

      6'b001100:
      begin
        n[99:96] <= n[35:32] >> 1;
        d[63:60] <= d[91:88] ;
      end

      6'b001101:
      begin
        n[39:36] <= n[99:96] << 1;
        d[7:4] <= d[99:96] ;
      end

      6'b001110:
      begin
        n[31:28] <= 2 + (n[39:36] >> 1);
        d[19:16] <= d[7:4] - 6;
      end

      6'b001111:
      begin
        n[103:100] <= n[31:28] - 1;
        d[35:32] <= d[19:16] + 6;
      end

      6'b010000:
      begin
        n[95:92] <= n[103:100] >> 1;
        d[107:104] <= d[35:32] ^ 1;
      end

      6'b010001:
      begin
        n[75:72] <= n[95:92] >> 1;
        d[115:112] <= d[107:104] ^ 1;
      end

      6'b010010:
      begin
        n[7:4] <= n[75:72] << 2;
        d[119:116] <= d[115:112] ^ 2;
      end

      6'b010011:
      begin
        n[23:20] <= n[7:4] << 1;
        d[95:92] <= d[119:116] - (10 >> 1);
      end

      6'b010100:
      begin
        n[115:112] <= n[23:20] + 5;
        d[55:52] <= d[95:92] + 2;
      end

      6'b010101:
      begin
        n[59:56] <= n[115:112] & 0;
        d[11:8] <= d[55:52] << 1;
      end

      6'b010110:
      begin
        n[79:76] <= n[59:56] + 3;
        d[75:72] <= 7 + (d[11:8] << 1);
      end

      6'b010111:
      begin
        n[55:52] <= n[79:76] << 2;
        d[87:84] <= d[75:72] ^ 9;
      end

      6'b011000:
      begin
        n[67:64] <= n[55:52] - 1;
        d[23:20] <= d[87:84] + 8;
      end

      6'b011001:
      begin
        n[15:12] <= n[67:64];
        d[103:100] <= d[23:20] ^ 7;
      end

      6'b011010:
      begin
        n[71:68] <= n[15:12] + (1 << 2);
        d[47:44] <= d[103:100] + (1 << 1);
      end

      6'b011011:
      begin
        n[63:60] <= n[71:68] >> 3;
        d[39:36] <= d[47:44] >> 1;
      end

      6'b011100:
      begin
        n[87:84] <= 2 + (n[63:60] << 3);
        d[31:28] <= d[39:36] + 1;
      end

      6'b011101:
      begin
        n[51:48] <= n[87:84] >> 3;
        d[51:48] <= d[31:28] >> 2;
      end

      6'b011110:
      begin
        n[119:116] <= 1 + (n[51:48] << 3);
        d[59:56] <= 3 + (d[51:48] << 2);
      end

      6'b011111:
      begin
        n[123:120] <= n[119:116] + 1;
        d[123:120] <= d[59:56] & 4;
      end

      6'b100000:
      begin
        n <= n;
        d <= d;
      end

      default:
      begin
        n <= 128'b0;
        d <= 128'b0;
      end
    endcase

    if (count < 32)
      count <= count + 1;
    else
    begin

      // TODO: modular exponentiation...

    end
  end
end

endmodule
