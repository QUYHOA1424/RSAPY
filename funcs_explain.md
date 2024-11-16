- Hàm tính lũy thừa a^b trên GF(m): powMod(a, b, m)
    - Hàm nhận ba tham số: a (cơ số), b (số mũ), và m (mô-đun), thực hiện phép tính: a^b (mod m)
    - Tính chất được áp dụng: [(a mod m) * (b mod m)] mod m = (a * b) mod m
    - Ý tưởng triển khai:
        + b = b0 + b1*2^1 + b2*2^2 + ... + bn*2^n
        + a^b = a^(b0 + b1*2^1 + b2*2^2 + ... + bn*2^n)
              = a^b0 * a^(b1*2^1) * a^( b2*2^2) * .... * a^(bn*2^n)
              = (a^(2^0))^b0 * (a^(2^1))^b1 * .... * (a^(2^n))^bn
        + Tính a^b (mod m) thông qua:
            * (a^(2^0))^b0 mod m
            * (a^(2^1))^b1 mod m
            ....................
            * (a^(2^n))^bn mod m
            * Nhân các kết quả phép tính phụ và thực hiện mod lần cuối
    - Hiện thực trong hàm:
        + Tính và lưu các hệ số b0, b1, b2,...bn vào danh sách thông qua phép and và phép dịch phải
        + Tính các số (a^(2^i)) % m (0 <= i <= n) thông qua vòng lặp với công thức: 
            x0 = a % m = (a^(2^0)) % m
            x1 = (x0 * x0) % m = (a%m * a%m) % m = a^2 % m = (a^(2^1)) % m
            x2 = (x1 * x1) % m = ((a^2)%m * (a^2)%m) % m = (a^(2^2)) % m
            ....................
        + Tính tích của các (a^(2^i))^bi mod m
         