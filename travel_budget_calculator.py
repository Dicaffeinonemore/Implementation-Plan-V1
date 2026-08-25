def calculate_remaining_budget(total_budget: int, flight_cost: int) -> int:
    return total_budget - flight_cost


def convert_krw_to_usd(remaining_budget: float, exchange_rate: float) -> float:
    return remaining_budget / exchange_rate


def main() -> None:
    # 1. 사용자에게 값 입력받기
    total_budget = int(input("전체 여행 예산을 입력하세요(원): "))
    flight_cost = int(input("항공권 가격을 입력하세요(원): "))
    exchange_rate = float(input("1달러당 환율을 입력하세요(원): "))

    # 2. 항공권을 제외한 남은 예산 계산
    remaining_budget = calculate_remaining_budget(
        total_budget,
        flight_cost
    )

    # 3. 남은 원화를 달러로 환산
    available_usd = convert_krw_to_usd(
        remaining_budget,
        exchange_rate
    )

    # 4. 결과 출력
    print()
    print(f"남은 예산: {remaining_budget:,.0f}원")
    print(f"사용 가능한 금액: 약 {available_usd:,.2f}달러")


if __name__ == "__main__":
    main()